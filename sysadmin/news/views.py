from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from  .models import News 
# Create your views here.
class News(TemplateView):
    model=News
    template_name= 'news.html'
