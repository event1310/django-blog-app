from django.contrib.sites import requests
from .views import post_detail, PostList
from django.http import HttpRequest

from . import views
from django.urls import path

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail,  name='post_detail'),
]