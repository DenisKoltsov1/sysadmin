from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from  .models import News 
from .forms import NewsForm




from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from .models import *

from django.forms import model_to_dict
# Create your views here.
class News(ListView):
    model=News
    template_name='news.html'


class CreateNews(UserPassesTestMixin,CreateView):
    model = News
    form_class = NewsForm
    template_name='news_form.html'
    success_url ='/news'

    def test_func(self):
        return self.request.user.is_staff


class NewsDetailView(LoginRequiredMixin, DetailView):
    model = News

class UpdateNews(UserPassesTestMixin, UpdateView):
    model = News
    form_class =NewsForm
    success_url ='/news'

    def test_func(self):
        return self.request.user.is_staff


class DeleteNews(UserPassesTestMixin, DeleteView):
    model = News
    template_name='news_confirm_delete.html'
    success_url ='/news'
    
    def test_func(self):
        return self.request.user.is_superuser




    def post(self,request):
        post_new = News.objects.create(
            id = request.data['id'],
            title =request.data['title'],
            content =request.data['content'],
            img = request.data['img']
        )
        return ({'post':model_to_dict(post_new)})