from django.urls import path
from . import views
from .api import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    # TODO seach and weight
    # TODO Validation Schemma
    # path('search', views.ResumeList.as_view()),
    path('list', views.ResumeList.as_view()),
    path('detail/<int:pk>/<slug:slug>', views.ResumeDetail.as_view()),
    path('me', views.MyResume.as_view()),
   

]

urlpatterns = format_suffix_patterns(urlpatterns)
