from django.urls import path
from . import views
from .api import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('gender', views.GenderList.as_view()),
    path('language/', views.LanguageList.as_view()),
    path('language/skill', views.LanguageSkillList.as_view()),
    path('province/', views.ProvincelList.as_view()),
    path('province/<int:pk>/city', views.CitylList.as_view()),
    path('benefit/job', views.BenefitlList.as_view()),
    path('military', views.MilitaryList.as_view()),
    path('marital/status', views.MaritalStatusList.as_view()),
    path('job/skill/', views.JobSkillList.as_view()),
    path('grade/', views.GradeList.as_view()),
    path('socialmedia/', views.SocialMediaList.as_view()),

    # path('category/detail/<int:pk>/<slug:slug>', views.CategoriesDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
