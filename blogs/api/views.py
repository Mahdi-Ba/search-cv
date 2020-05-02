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

class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class Categories(APIView):
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

    def get(self, request, pk, slug, format=None):
        category = self.get_object(pk)
        serializer = CategorySerilizer(category)
        return Response(serializer.data)


class Tags(APIView):
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

    def get(self, request, pk, slug, format=None):
        tag = self.get_object(pk)
        serializer = TagSerilizer(tag)
        return Response(serializer.data)


class Articles(APIView):
    pagination_class = BasicPagination

    def get(self, request, format=None):
        articles = Article.objects.all()
        articles_serlizer = ArticleSerilizer(articles, many=True)
        return Response(articles_serlizer.data)

    def post(self, request, format=None):
        SearchLog.objects.create(user=request.user,title=request.data['item'])
        articles = Article.objects.filter(Q(title__contains=request.data['item']) | Q(en_title__contains=request.data['item'])).all()
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

    def get(self, request, pk, slug, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerilizer(article, many=True)
        return Response(serializer.data)



class ArticleCategorysSearch(APIView):
    def get_object(self, pk):
        try:
            article = Article.objects.filter(category=pk).all()
            return article
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request, pk, slug, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerilizer(article, many=True)
        return Response(serializer.data)
