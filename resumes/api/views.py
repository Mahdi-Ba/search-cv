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



class MyResume(APIView):
    @swagger_auto_schema(
        operation_description="get MyResume",
        responses={200: ResumeDetailSerilizer(many=True)}
    )
    def get(self, request, format=None):
        if Resume.objects.filter(owner=request.user).exists():
            resume = Resume.objects.get(owner=request.user)
            resume_serlizer = ResumeDetailSerilizer(resume)
            return Response(resume_serlizer.data)
        else:
            return Response({"status":False},status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description="delete",
        responses={200:openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
           'items': openapi.Schema(
              type=openapi.TYPE_STRING
           )}
    )})
    def delete(self,request,format=None):
        resume = Resume.objects.get(owner=request.user)
        self.deleteElastic(resume)
        resume.delete()
        return Response({"items":"deleted"},status=status.HTTP_200_OK)

    @swagger_auto_schema(
            operation_description="""
        مثال        
                        {
                            "text": "saladccfrffr",
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
                                    },
                                  {
                                        "id": 2,
                                        "title": "runner"
                                    }
                                ]
                            }
                """,
            request_body=ResumeDetailSerilizer,
            responses={200: ResumeDetailSerilizer(many=True)}

    )
    def put(self, request ,format=None):
        valid = True
        if request.data.get('info',False):
            valid = jsonschema.Draft7Validator(SCHMMA).is_valid(request.data['info'])
        if valid:
            if Resume.objects.filter(owner=request.user).exists():
                resume_model = Resume.objects.get(owner=request.user)
                resume = ResumeDetailSerilizer(resume_model, data=request.data)
                if resume.is_valid():
                    resume.save()
                    self.saveElastic(resume.data)
                    return Response(resume.data, status=status.HTTP_200_OK)
                return Response(resume.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"status": False, "message": "bad request"},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"status": False, "message": "validation error request"},
                            status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
            operation_description="""
    مثال        

                       {
                            "text": "sala",
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
            request_body=ResumeDetailSerilizer,
            responses = {200: ResumeDetailSerilizer(many=True)}

    )
    def post(self, request, format=None):
        # valid  = jsonschema.Draft7Validator(SCHMMA).is_valid(request.data['info'])
        # if valid == True:
        if True:
            if not Resume.objects.filter(owner=request.user).exists():
                resume = ResumeDetailSerilizer(data=request.data)
                if resume.is_valid():
                    resume.save(owner=request.user)
                    self.saveElastic(resume.data)
                    return Response(resume.data, status=status.HTTP_200_OK)
                return Response(resume.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"status":False,"message":"bad request"},status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"status":False,"message":"validation error request"},status=status.HTTP_400_BAD_REQUEST)

    def saveElastic(self,obj):
        elastic_data = obj["info"]
        elastic_host = {"host": "localhost", "port": 9200}
        es = Elasticsearch(hosts=[elastic_host])
        es.index(index='resume', doc_type='person', id=obj["id"], body=elastic_data)

    def deleteElastic(self,obj):
        elastic_host = {"host": "localhost", "port": 9200}
        es = Elasticsearch(hosts=[elastic_host])
        es.delete(index='resume', doc_type='person', id=obj.id)


class ResumeDetail(APIView):
    @swagger_auto_schema(
        operation_description="get advertise detail",
        responses={200: ResumeDetailSerilizer(many=False)}
    )
    def get(self, request,pk,slug, format=None):
        resume = Resume.objects.get(pk=pk)
        resume_serlizer = ResumeDetailSerilizer(resume)
        return Response(resume_serlizer.data)



class ResumeList(APIView,PaginationHandlerMixin):
    pagination_class = BasicPagination

    @swagger_auto_schema(
        operation_description="get advertise pagination",
        responses={200: ResumeDetailSerilizer(many=True)}
    )
    def get(self, request, format=None):
        resume = Resume.objects.order_by('-updated_at').all()
        page = self.paginate_queryset(resume)
        if page is not None:
            resume_serlizer = self.get_paginated_response(ResumeDetailSerilizer(page,many=True).data)
        else:
            resume_serlizer = ResumeDetailSerilizer(resume, many=True)
        return Response(resume_serlizer.data)

