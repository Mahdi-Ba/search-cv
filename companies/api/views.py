import base64
import uuid

from django.core.files.base import ContentFile
from django.db.models import Q
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from ..models import *
from rest_framework.pagination import PageNumberPagination
from talent.pagination import PaginationHandlerMixin
from drf_yasg.utils import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'



class MyCompany(APIView):
    @swagger_auto_schema(
        responses={200: CompanyDetailSerilizer(many=False)}
    )
    def get(self, request, format=None):
        company = Company.objects.filter(owner=request.user).all()
        company_serlizer = CompanyDetailSerilizer(company, many=True)
        return Response(company_serlizer.data)


class InsertMyCompany(APIView):
    @swagger_auto_schema(
        operation_description="""
    مثال        

                     {
                        "title": "test",
                        "en_title": "test",
                        "address":"tehran iran",
                        "phone":"77426868",
                        "text": "descrption ....",
                        "company_size":1,
                        "parent_Company":30,
                        "working_area_Company":[2,3,4],
                        "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyZpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQyIDc5LjE2MDkyNCwgMjAxNy8wNy8xMy0wMTowNjozOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTggKFdpbmRvd3MpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkEyRkNGMUNDNTE1QTExRUE5MzEyOTlBNzEyNDRBODY3IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkEyRkNGMUNENTE1QTExRUE5MzEyOTlBNzEyNDRBODY3Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6QTJGQ0YxQ0E1MTVBMTFFQTkzMTI5OUE3MTI0NEE4NjciIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6QTJGQ0YxQ0I1MTVBMTFFQTkzMTI5OUE3MTI0NEE4NjciLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz7vf6n0AAAEgElEQVR42uxaWWxMURi+U2NpSz2g9tIqLUJJE0vtSkI86AtphFge8GBJbZVaprU0qK2WkEgaopoGEQ+kkVSEWopIqwmKrppoQkMoVZ17z/Wdmf9ylEln7lLKnOTL+c9dzr3fPef/z/efGVtqaqr0L5QA6R8pfiJ+In4i/wkRm1kdDcmpnMyYullV2VSVqYGAhLakqgBzgzHmtlWtTedUprUV1CU4fw718fpt4xpbeq62fBgekejz1fao3KpMmDeB2UCgge7aAaOB/cCj4LS7/b290W6ExNALr0Lw9S7CnCkcrgIe65zmYUAMtYcB14Icd2Ib0iZ8sZQISrJAwglsBI5VLB6s6O2wa/qDUaguAeH8WwEpwDarnb2G6vdAfNnCiMzyRZGKkQ4/pIwpRpUAaP1sDNx+O9xSIs/mhZ2kOR35YkF4gVmB4+OWsSV8ZKnZEThoefgtnT+g+HniwHcWRFQH8JbshE5bC2a0yXUEofcD+YdWjnRIuWXX5eyISjZFViQXnEz6bstum2m2U/n5XMY01SQ+WcBKIJYcfxVw2OsRAYFQoA4m04Wk/FogxCiLz4443t9qcf1rv/lmqC9Tqx/QzcA79AJ6mjEkWEPuocrWojOQ7svU4gvacqC7zufXAuUmukwyheTOwDL7phsn5H3THlmitawuiFrJ0GJ73LqNFUJRxCkZ01XTtFYrlkNAGdnjgIU/jQicOpovamBoY4qLLalS1D/agVCuNmjT7wqWaWpWPKYI9/7aB7+uUVIhPw7NaNDDBOF3Dp5zhfeH961Fn1GOLgX1mo88pLnXWoWr41N6bmxKn3wVUSuPVHZvYC2wS5taj1uRBA+nLwz2sV6wE8WoNYn0jCfHV+kFzCgKppUhUencM+UZotYTmMNJ6ruJQPjxF22U2njxOh/hSRSqUC5D5CZZlpsUJjtlbgM45ra14wyOX4evz8x+YfjIUDj7cGo+9YkISPDrXgPBPjzzNLDUgo9/QLBzfVW/ekRgP7MZ8PBLEUtTD5k+jQj8SMGo8CytrzbCtFHwy7Po43CHLjF5Ze+AdUNUvsnqgfh6iVZ2r30EZN4Kic6fKEk8EyW7UBCSbUeiIGfvg2qrMM1XcZ3lMWqRXLmNS7spiuKSHDxRckkPgiuh4jVvyx6Ou881QEbMReTKN4HLXkF9ZDVXvr8bkVEG8xCxBPGdFcOdOO6MFwRi8/TX4zqSR4mLGdrrK3DCSAfBaXcDIBKPihkiVvY3LRKBQ3PGW/4i91hG+brr9YQtorazi9JlZ2HztHYN1K9sGZHo89VhUblVdgu4pAE9yL7cuGtSvmX7WohyfBpW88VvSE5lpFkMQnbfH0lbP5qvrWvpHqMjMkLjBBRFZlesGHS2zFCftIl9WVAOGV92TKw0Tf16KClEZhhFOr4XnBRx5mWpjh96AtAOQx0jxh9P2z+mEkGUq4CPjKVospgORxGMFi7RZ3nz24gpzl46f8Cn54kDl9Did91gksbFZhGwgYfdz464Gm9vtPn/wuEn4ifiJ+In8ifKNwEGAAQ3e05UQwu0AAAAAElFTkSuQmCC"
                     }
            """,
        request_body=CompanyDetailSerilizer,
        responses={200: CompanyDetailSerilizer(many=False)}
    )
    def post(self, request, format=None):
        if request.data.get('image',False):
            base64_file = request.data.pop('image')
            format, imgstr = base64_file.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=str(uuid.uuid4()) + "." + ext)
            request.data['image'] = data
        company = CompanyDetailSerilizer(data=request.data)
        if company.is_valid():
            company.save(owner=request.user)
            return Response(company.data, status=status.HTTP_200_OK)
        return Response(company.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateMyCompany(APIView):
    @swagger_auto_schema(
        operation_description="""
    مثال        
                     {
                        "title": "test",
                        "en_title": "test",
                        "address":"tehran iran",
                        "phone":"77426868",
                        "text": "descrption ....",
                        "company_size":1,
                        "parent_Company":30,
                        "working_area_Company":[2,3,4],
                        "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyZpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQyIDc5LjE2MDkyNCwgMjAxNy8wNy8xMy0wMTowNjozOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTggKFdpbmRvd3MpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkEyRkNGMUNDNTE1QTExRUE5MzEyOTlBNzEyNDRBODY3IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkEyRkNGMUNENTE1QTExRUE5MzEyOTlBNzEyNDRBODY3Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6QTJGQ0YxQ0E1MTVBMTFFQTkzMTI5OUE3MTI0NEE4NjciIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6QTJGQ0YxQ0I1MTVBMTFFQTkzMTI5OUE3MTI0NEE4NjciLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz7vf6n0AAAEgElEQVR42uxaWWxMURi+U2NpSz2g9tIqLUJJE0vtSkI86AtphFge8GBJbZVaprU0qK2WkEgaopoGEQ+kkVSEWopIqwmKrppoQkMoVZ17z/Wdmf9ylEln7lLKnOTL+c9dzr3fPef/z/efGVtqaqr0L5QA6R8pfiJ+In4i/wkRm1kdDcmpnMyYullV2VSVqYGAhLakqgBzgzHmtlWtTedUprUV1CU4fw718fpt4xpbeq62fBgekejz1fao3KpMmDeB2UCgge7aAaOB/cCj4LS7/b290W6ExNALr0Lw9S7CnCkcrgIe65zmYUAMtYcB14Icd2Ib0iZ8sZQISrJAwglsBI5VLB6s6O2wa/qDUaguAeH8WwEpwDarnb2G6vdAfNnCiMzyRZGKkQ4/pIwpRpUAaP1sDNx+O9xSIs/mhZ2kOR35YkF4gVmB4+OWsSV8ZKnZEThoefgtnT+g+HniwHcWRFQH8JbshE5bC2a0yXUEofcD+YdWjnRIuWXX5eyISjZFViQXnEz6bstum2m2U/n5XMY01SQ+WcBKIJYcfxVw2OsRAYFQoA4m04Wk/FogxCiLz4443t9qcf1rv/lmqC9Tqx/QzcA79AJ6mjEkWEPuocrWojOQ7svU4gvacqC7zufXAuUmukwyheTOwDL7phsn5H3THlmitawuiFrJ0GJ73LqNFUJRxCkZ01XTtFYrlkNAGdnjgIU/jQicOpovamBoY4qLLalS1D/agVCuNmjT7wqWaWpWPKYI9/7aB7+uUVIhPw7NaNDDBOF3Dp5zhfeH961Fn1GOLgX1mo88pLnXWoWr41N6bmxKn3wVUSuPVHZvYC2wS5taj1uRBA+nLwz2sV6wE8WoNYn0jCfHV+kFzCgKppUhUencM+UZotYTmMNJ6ruJQPjxF22U2njxOh/hSRSqUC5D5CZZlpsUJjtlbgM45ra14wyOX4evz8x+YfjIUDj7cGo+9YkISPDrXgPBPjzzNLDUgo9/QLBzfVW/ekRgP7MZ8PBLEUtTD5k+jQj8SMGo8CytrzbCtFHwy7Po43CHLjF5Ze+AdUNUvsnqgfh6iVZ2r30EZN4Kic6fKEk8EyW7UBCSbUeiIGfvg2qrMM1XcZ3lMWqRXLmNS7spiuKSHDxRckkPgiuh4jVvyx6Ou881QEbMReTKN4HLXkF9ZDVXvr8bkVEG8xCxBPGdFcOdOO6MFwRi8/TX4zqSR4mLGdrrK3DCSAfBaXcDIBKPihkiVvY3LRKBQ3PGW/4i91hG+brr9YQtorazi9JlZ2HztHYN1K9sGZHo89VhUblVdgu4pAE9yL7cuGtSvmX7WohyfBpW88VvSE5lpFkMQnbfH0lbP5qvrWvpHqMjMkLjBBRFZlesGHS2zFCftIl9WVAOGV92TKw0Tf16KClEZhhFOr4XnBRx5mWpjh96AtAOQx0jxh9P2z+mEkGUq4CPjKVospgORxGMFi7RZ3nz24gpzl46f8Cn54kDl9Did91gksbFZhGwgYfdz464Gm9vtPn/wuEn4ifiJ+In8ifKNwEGAAQ3e05UQwu0AAAAAElFTkSuQmCC"
                     }
            """,
        request_body=CompanyDetailSerilizer,
        responses={200: CompanyDetailSerilizer(many=False)}
    )
    def put(self, request,pk ,format=None):
        company_model = Company.objects.get(pk=pk,owner=request.user)
        if company_model != None:
            if request.data.get('image', False):
                base64_file = request.data.pop('image')
                format, imgstr = base64_file.split(';base64,')
                ext = format.split('/')[-1]
                data = ContentFile(base64.b64decode(imgstr), name=str(uuid.uuid4()) + "." + ext)
                request.data['image'] = data
            company = CompanyDetailSerilizer(company_model,data=request.data)
            if company.is_valid():
                company.save()
                return Response(company.data, status=status.HTTP_200_OK)
            return Response(company.errors, status=status.HTTP_400_BAD_REQUEST)





class CompanyDetail(APIView):
    @swagger_auto_schema(
        operation_description="get CompanyDetailSerilizer",
        responses={200: CompanyDetailSerilizer(many=True)}
    )
    def get(self, request,pk,slug, format=None):
        company = Company.objects.filter(pk=pk).all()
        company_serlizer = CompanyDetailSerilizer(company, many=True)
        return Response(company_serlizer.data)



class CompanyIndex(APIView):
    @swagger_auto_schema(
        operation_description="get CompanyIndex",
        responses={200: CompanyDetailSerilizer(many=True)}
    )
    def get(self, request, format=None):
        company = Company.objects.filter(index=True).all()
        company_serlizer = CompanyDetailSerilizer(company, many=True)
        return Response(company_serlizer.data)

class CompanyList(APIView,PaginationHandlerMixin):
    pagination_class = BasicPagination

    @swagger_auto_schema(responses={200: CompanyDetailSerilizer(many=True)})
    def get(self, request, format=None):
        company = Company.objects.all()
        page = self.paginate_queryset(company)
        if page is not None:
            company_serlizer = self.get_paginated_response(CompanyDetailSerilizer(page,many=True).data)
        else:
            company_serlizer = CompanyDetailSerilizer(company, many=True)
        return Response(company_serlizer.data)

    @swagger_auto_schema(responses={200: CompanySerilizer(many=True)})
    def post(self, request, format=None):
        company = Company.objects.filter(Q(title__contains=request.data['item']) | Q(en_title__contains=request.data['item'])).all()
        page = self.paginate_queryset(company)
        if page is not None:
            company_serlizer = self.get_paginated_response(CompanySerilizer(page, many=True).data)
        else:
            company_serlizer = CompanySerilizer(company, many=True)
        return Response(company_serlizer.data)


class CompanySearch(APIView,PaginationHandlerMixin):
    pagination_class = BasicPagination

    @swagger_auto_schema(
        operation_description="apiview search ",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['item'],
            properties={
                'item': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        responses={200: CompanySerilizer(many=True)}
    )
    def post(self, request, format=None):
        company = Company.objects.filter(Q(title__contains=request.data['item']) | Q(en_title__contains=request.data['item'])).all()
        page = self.paginate_queryset(company)
        if page is not None:
            company_serlizer = self.get_paginated_response(CompanySerilizer(page, many=True).data)
        else:
            company_serlizer = CompanySerilizer(company, many=True)
        return Response(company_serlizer.data)

class CompanySelect(APIView):
    @swagger_auto_schema(
        operation_description="apiview search ",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['item'],
            properties={
                'item': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        responses={200: CompanySerilizer(many=True)}
    )
    def post(self, request, format=None):
            company = Company.objects.filter(
                Q(title__contains=request.data['item']) | Q(en_title__contains=request.data['item'])).all()[:14]
            company_serlizer = CompanySerilizer(company, many=True)
            return Response(company_serlizer.data)
#
#
#
# class ArticlesDetail(APIView):
#     def get_object(self, pk):
#         try:
#             article = Article.objects.get(pk=pk)
#             article.visit = article.visit + 1
#             article.save()
#             return article
#         except Tag.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, slug, format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerilizer(article)
#         return Response(serializer.data)
#

