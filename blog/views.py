from django.shortcuts import render
from django.views import generic
from .models import BlogPost
# Create your views here.

class BlogListView(generic.ListView):
    model = BlogPost

class BlogDetailView(generic.DetailView):
    model = BlogPost