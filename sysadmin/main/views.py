from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Main(TemplateView):
    template_name= 'main.html'