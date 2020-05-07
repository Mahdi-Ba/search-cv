from django.db.models import Q
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers import Page, PageSerializer, PageContentSerializer
from .serializers import CategorySerilizer, TagSerilizer, ArticleSerilizer
from ..models import Article, Category, Tag, SearchLog
from rest_framework.pagination import PageNumberPagination
from talent.pagination import PaginationHandlerMixin
from drf_yasg.utils import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view



class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class Categories(APIView):
    @swagger_auto_schema(
        operation_description="get category",
        responses={200: CategorySerilizer(many=True)}
    )
    def get(self, request, format=None):
        categories = Category.objects.all()
        category_serlizer = CategorySerilizer(categories, many=True)
        return Response(category_serlizer.data)


class CategoriesDetail(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
    @swagger_auto_schema(
        operation_description="get category",
        responses={200: CategorySerilizer(many=False)}
    )
    def get(self, request, pk, slug, format=None):
        category = self.get_object(pk)
        serializer = CategorySerilizer(category)
        return Response(serializer.data)


class Tags(APIView):
    @swagger_auto_schema(
        operation_description="gettag",
        responses={200: TagSerilizer(many=True)}
    )
    def get(self, request, format=None):
        Tags = Tag.objects.all()
        Tags_serlizer = TagSerilizer(Tags, many=True)
        return Response(Tags_serlizer.data)


class TagsDetail(APIView):
    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="get category",
        responses={200: TagSerilizer(many=False)}
    )
    def get(self, request, pk, slug, format=None):
        tag = self.get_object(pk)
        serializer = TagSerilizer(tag)
        return Response(serializer.data)


class ArticlesIndex(APIView):
    @swagger_auto_schema(
        operation_description="Pagination ",
        responses={200: ArticleSerilizer(many=True)}
    )
    def get(self, request, format=None):
        articles = Article.objects.filter(index=True).all()
        articles_serlizer = ArticleSerilizer(articles, many=True)
        return Response(articles_serlizer.data)

class Articles(APIView,PaginationHandlerMixin):
    pagination_class = BasicPagination

    @swagger_auto_schema(
        operation_description="Pagination ",
        responses={200: ArticleSerilizer(many=True)}
    )
    def get(self, request, format=None):
        articles = Article.objects.all()
        page = self.paginate_queryset(articles)
        if page is not None:
            articles_serlizer = self.get_paginated_response(ArticleSerilizer(page,many=True).data)
        else:
            articles_serlizer = ArticleSerilizer(articles, many=True)
        return Response(articles_serlizer.data)

    @swagger_auto_schema(
        operation_description="apiview search ",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['item'],
            properties={
                'item': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        responses={200: ArticleSerilizer(many=True)}
    )
    def post(self, request, format=None):
        SearchLog.objects.create(user=request.user,title=request.data['item'])
        articles = Article.objects.filter(Q(title__contains=request.data['item']) | Q(en_title__contains=request.data['item'])).all()
        page = self.paginate_queryset(articles)
        if page is not None:
            articles_serlizer = self.get_paginated_response(ArticleSerilizer(page, many=True).data)
        else:
            articles_serlizer = ArticleSerilizer(articles, many=True)
        return Response(articles_serlizer.data)



class ArticlesDetail(APIView):
    def get_object(self, pk):
        try:
            article = Article.objects.get(pk=pk)
            article.visit = article.visit + 1
            article.save()
            return article
        except Tag.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="article detail ",
        responses={200: ArticleSerilizer(many=False)}
    )
    def get(self, request, pk, slug, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerilizer(article)
        return Response(serializer.data)


class ArticleTagsSearch(APIView):
    def get_object(self, pk):
        try:
            article = Article.objects.filter(tag=pk).all()
            return article
        except Tag.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="get artcle per tag",
        responses={200: ArticleSerilizer(many=True)}
    )
    def get(self, request, pk, slug, format=None):
        articles = self.get_object(pk)
        page = self.paginate_queryset(articles)
        if page is not None:
            articles_serlizer = self.get_paginated_response(ArticleSerilizer(page, many=True).data)
        else:
            articles_serlizer = ArticleSerilizer(articles, many=True)
        return Response(articles_serlizer.data)




class ArticleCategorysSearch(APIView,PaginationHandlerMixin):
    pagination_class = BasicPagination

    def get_object(self, pk):
        try:
            article = Article.objects.filter(category=pk).all()
            return article
        except Tag.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_description="apiview post ",
        responses={200: ArticleSerilizer(many=True)}
    )
    def get(self, request, pk, slug, format=None):
        articles = self.get_object(pk)
        page = self.paginate_queryset(articles)
        if page is not None:
            articles_serlizer = self.get_paginated_response(ArticleSerilizer(page, many=True).data)
        else:
            articles_serlizer = ArticleSerilizer(articles, many=True)
        return Response(articles_serlizer.data)

