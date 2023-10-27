from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from  .models import News 
from .forms import NewsForm
# Create your views here.
class News(TemplateView):
    model=News
    template_name= 'news.html'


class CreateNews(UserPassesTestMixin,CreateView):
    model = News

    form_class = NewsForm
    
    success_url = '/create_news'

    def test_func(self):
        return self.request.user.is_staff
