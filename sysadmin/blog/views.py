
from blog.models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from blog.forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from django.http import HttpResponse

import requests


import requests

class Blog(ListView):
    model = Blog
    
    template_name ='blog.html'
    queryset  = Blog.objects.all()


class BlogCreate(UserPassesTestMixin,CreateView):
    model = Blog
    form_class = BlogForm
    success_url = '/blog'
    template_name = 'blog_form.html'

    def test_func(self):
        return self.request.user.is_staff