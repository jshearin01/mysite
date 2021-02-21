from django.shortcuts import render
from django.views import generic
from .models import BlogPost, Persona
# Create your views here.

class BlogListView(generic.ListView):
    model = BlogPost
    ordering = ['-created_time']

class BlogDetailView(generic.DetailView):
    model = BlogPost

class PersonaListView(generic.ListView):
    model = Persona
    
class PersonaDetailView(generic.DetailView):
    model = Persona
