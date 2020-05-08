import base64
import uuid

from django.core.files.base import ContentFile
from django.db.models import Q
from django.http import Http404
from elasticsearch import Elasticsearch
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .schemma import SCHMMA
from .serializers import *
from ..models import *
from rest_framework.pagination import PageNumberPagination
from talent.pagination import PaginationHandlerMixin
import jsonschema
from drf_yasg.utils import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class MixinElastic:
    def saveElastic(self, obj):
        elastic_data = obj["info"]
        elastic_host = {"host": "localhost", "port": 9200}
        es = Elasticsearch(hosts=[elastic_host])
        es.index(index='advertises', doc_type='advertise', id=obj["id"], body=elastic_data)

    def deleteElastic(self, obj):
        elastic_host = {"host": "localhost", "port": 9200}
        es = Elasticsearch(hosts=[elastic_host])
        es.delete(index='advertises', doc_type='advertise', id=obj.id)


class MyAdvertise(APIView, MixinElastic):


    @swagger_auto_schema(
        operation_description="get advertises",
        responses={200: AdvertiseDetailSerilizer(many=True)}
    )
    def get(self, request, format=None):
        advertise = Advertise.objects.filter(owner=request.user).all()
        advertise_serlizer = AdvertiseDetailSerilizer(advertise, many=True)
        return Response(advertise_serlizer.data)

    @swagger_auto_schema(
        operation_description="delete",
        responses={200:openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
           'items': openapi.Schema(
              type=openapi.TYPE_STRING
           )}
    )})
    def delete(self, request, format=None):
        advertise = Advertise.objects.filter(owner=request.user).all()
        for item in advertise:
            self.deleteElastic(item)
            item.delete()
        return Response({"items":"deleted"},status=status.HTTP_200_OK)


class AdvertiseUpdate(APIView, MixinElastic):
    @swagger_auto_schema(
        operation_description="""
برای ویرایش companyکمپانی ارسال نشود
 درصورتی که title , en_title تغییر نکردند نیازی به ارسال نیست 
  در صورتی که میخواهید کمپانی NULL شود zمقدار company_src = -1 ست شود 
    تمامی info ها هر بار در صورت کوچک ترین تغییر ارسال گردد

                                 {
                                    "title": "تست",
                                    "en_title": "test",
                                    "company_src": -1,
                                    "text": "text descriptio",
                                    "info": {
                                        "gender": {
                                            "id": 1,
                                            "title": "woman"
                                        },
                                        "ability": [
                                            {
                                                "id": 1,
                                                "title": "barber"
                                            },
                                            {
                                                "id": 2,
                                                "title": "swimmer"
                                            }
                                     
                                        ]
                                }
            """,
        request_body=AdvertiseDetailSerilizer,
        responses={200: AdvertiseDetailSerilizer(many=False)}
    )
    def put(self, request, pk, format=None):
        valid = True
        if request.data.get('info', False):
            valid = jsonschema.Draft7Validator(SCHMMA).is_valid(request.data['info'])
        if valid:
            if Advertise.objects.filter(owner=request.user, pk=pk).exists():
                advertise_model = Advertise.objects.get(owner=request.user, pk=pk)
                advertise = AdvertiseDetailSerilizer(advertise_model, data=request.data)
                if advertise.is_valid():
                    advertise.save()
                    self.saveElastic(advertise.data)
                    return Response(advertise.data, status=status.HTTP_200_OK)
                return Response(advertise.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"status": False, "message": "bad request"},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"status": False, "message": "validation error request"},
                            status=status.HTTP_400_BAD_REQUEST)


class AdvertiseInsert(APIView, MixinElastic):
    @swagger_auto_schema(
        operation_description="""
کمپانی ارسال نشود
info شامل تمام موارد میشود
company_src ایدی کمپانی مورد نظر است
مثال        

                    {	
                        "title":"تست",
                        "en_title":"TEST",
                        "company_src":31,
                        "text": "test",
                        "info": {
                            "gender": {
                                "id": 1,
                                "title": "woman"
                            },
                            "ability": [
                                {
                                    "id": 1,
                                    "title": "barber"
                                },
                                {
                                    "id": 2,
                                    "title": "swimmer"
                                }
                            ]
                        }
                    }
        """,
        request_body=AdvertiseDetailSerilizer,
        responses={200: AdvertiseDetailSerilizer(many=True)}
    )
    def post(self, request, format=None):
        # valid  = jsonschema.Draft7Validator(SCHMMA).is_valid(request.data['info'])
        # if valid == True:
        if True:
            advertise = AdvertiseDetailSerilizer(data=request.data)
            if advertise.is_valid():
                advertise.save(owner=request.user)
                self.saveElastic(advertise.data)
                return Response(advertise.data, status=status.HTTP_200_OK)
            return Response(advertise.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": False, "message": "validation error request"},
                            status=status.HTTP_400_BAD_REQUEST)



class AdvertiseDetail(APIView):
    @swagger_auto_schema(
        operation_description="get advertise detail",
        responses={200: AdvertiseDetailSerilizer(many=False)}
    )
    def get(self, request, pk, slug, format=None):
        advertise = Advertise.objects.get(pk=pk)
        advertise_serlizer = AdvertiseDetailSerilizer(advertise)
        return Response(advertise_serlizer.data)


class AdvertiseList(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination

    @swagger_auto_schema(
        operation_description="get advertise pagination",
        responses={200: AdvertiseDetailSerilizer(many=True)}
    )
    def get(self, request):
        advertise = Advertise.objects.order_by('-updated_at').all()
        page = self.paginate_queryset(advertise)
        if page is not None:
            advertise_serlizer = self.get_paginated_response(AdvertiseDetailSerilizer(page, many=True).data)
        else:
            advertise_serlizer = AdvertiseDetailSerilizer(advertise, many=True)
        return Response(advertise_serlizer.data)
