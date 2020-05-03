from django.urls import path
from . import views
from .api import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [

    path('search/select', views.CompanySelect.as_view()),
    path('search', views.CompanyList.as_view()),
    path('list', views.CompanyList.as_view()),
    path('index', views.CompanyIndex.as_view()),

    path('detail/<int:pk>/<slug:slug>', views.CompanyDetail.as_view()),
    path('detail/me', views.MyCompany.as_view()),
    path('insert', views.MyCompany.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
