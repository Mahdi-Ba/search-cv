from django.urls import path
from . import views
from .api import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    # TODO seach and weight
    # TODO Validation Schemma
    # path('search', views.ResumeList.as_view()),
    path('list', views.AdvertiseList.as_view()),
    path('detail/<int:pk>/<slug:slug>', views.AdvertiseDetail.as_view()),
    path('detail/me', views.MyAdvertise.as_view()),
    path('insert', views.MyAdvertise.as_view()),
    path('update/<int:pk>', views.MyAdvertise.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
