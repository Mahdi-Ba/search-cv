from django.urls import path
from . import views
from .api import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('categories', views.Categories.as_view()),
    path('category/detail/<int:pk>/<slug:slug>', views.CategoriesDetail.as_view()),

    path('tags', views.Tags.as_view()),
    path('tag/detail/<int:pk>/<slug:slug>', views.TagsDetail.as_view()),

    path('articles', views.Articles.as_view()),
    path('articles/index', views.ArticlesIndex.as_view()),
    path('articles/detail/<int:pk>/<slug:slug>', views.ArticlesDetail.as_view()),

    path('articles/tag/<int:pk>/<slug:slug>', views.ArticleTagsSearch.as_view()),
    path('articles/category/<int:pk>/<slug:slug>', views.ArticleCategorysSearch.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
