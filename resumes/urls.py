from django.urls import path
from . import views
from .api import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    # TODO seach and weight
    # path('search', views.ResumeList.as_view()),
    path('list', views.ResumeList.as_view()),
    path('detail/<int:pk>/<slug:slug>', views.ResumeDetail.as_view()),
    path('detail/me', views.MyResume.as_view()),
    path('insert', views.MyResume.as_view()),
    path('update', views.MyResume.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
