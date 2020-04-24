from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers import Page, PageSerializer, PageContentSerializer
from ..models import Article
from rest_framework import status
import json
from django.core import serializers
import requests
# assuming obj is a model instance

# class PageList(APIView):
#     def get(self, request, format=None):
#         serialized_obj = serializers.serialize('json',[Article.objects.filter().first()])
#         requests.post('http://localhost:9200/mahdi/mahdi/1/',json=serialized_obj)
#         return Response("skjk")
#
