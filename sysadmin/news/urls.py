from django.contrib import admin
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *
urlpatterns = [
   
    path('', News.as_view(), name='news'),
    path('create_news/', CreateNews.as_view(), name='create_news'),
   ]

