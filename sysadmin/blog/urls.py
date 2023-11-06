from django.contrib import admin
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *
urlpatterns = [
   
    path('', Blog.as_view(), name='blog'),
    path('blog-create/',BlogCreate.as_view()),
   ]


