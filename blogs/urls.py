from django.urls import path
from . import views
from .api import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns


#
# urlpatterns = [
#     path('test', views.PageList.as_view()),
#
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
