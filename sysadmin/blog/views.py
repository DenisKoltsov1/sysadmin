from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from blog.forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from django.http import HttpResponse

import requests

class Blog(ListView):
    models = Blog
    template_name = 'blog.html'