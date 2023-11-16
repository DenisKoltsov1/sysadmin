from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from  .models import News 
from .forms import NewsForm





from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from .models import *

from django.forms import model_to_dict
# Create your views here.


class NewsList(ListView):
    model = News
    template_name='news.html'



class CreateNews(UserPassesTestMixin,CreateView):
    model = News
    form_class = NewsForm
    template_name='news_form.html'
    success_url ='/'

    def test_func(self):
        return self.request.user.is_staff





class NewsDelete(UserPassesTestMixin,DeleteView):
    model = News    
    success_url ='/'
    template_name='news_delete.html'
    def test_func(self):
        return self.request.user.is_staff

class UpdateNews(UserPassesTestMixin,UpdateView):
    model = News
    form_class = NewsForm
    template_name='news_form.html'
    success_url ='/'

    def test_func(self):
        return self.request.user.is_staff



    
class NewsDetailView(LoginRequiredMixin,DetailView):
    model = News
    template_name='news_detail.html'

    def test_func(self):
        return self.request.user.is_staff

