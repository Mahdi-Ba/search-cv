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

class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'



class MyCompany(APIView):
    def get(self, request, format=None):
        company = Company.objects.filter(owner=request.user).all()
        company_serlizer = CompanyDetailSerilizer(company, many=True)
        return Response(company_serlizer.data)

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

class CompanyDetail(APIView):
    def get(self, request,pk,slug, format=None):
        company = Company.objects.filter(pk=pk).all()
        company_serlizer = CompanyDetailSerilizer(company, many=True)
        return Response(company_serlizer.data)



class CompanyIndex(APIView):
    def get(self, request, format=None):
        company = Company.objects.filter(index=True).all()
        company_serlizer = CompanyDetailSerilizer(company, many=True)
        return Response(company_serlizer.data)

class CompanyList(APIView,PaginationHandlerMixin):
    pagination_class = BasicPagination

    def get(self, request, format=None):
        company = Company.objects.all()
        page = self.paginate_queryset(company)
        if page is not None:
            company_serlizer = self.get_paginated_response(CompanyDetailSerilizer(page,many=True).data)
        else:
            company_serlizer = CompanyDetailSerilizer(company, many=True)
        return Response(company_serlizer.data)

    def post(self, request, format=None):
        company = Company.objects.filter(Q(title__contains=request.data['item']) | Q(en_title__contains=request.data['item'])).all()
        page = self.paginate_queryset(company)
        if page is not None:
            company_serlizer = self.get_paginated_response(CompanySerilizer(page, many=True).data)
        else:
            company_serlizer = CompanySerilizer(company, many=True)
        return Response(company_serlizer.data)

class CompanySelect(APIView):
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

