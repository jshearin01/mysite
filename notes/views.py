from django.shortcuts import render
from django.views import generic
from .models import Note

# Create your views here.

class NoteListView(generic.ListView):
    model = Note

class NoteDetailView(generic.DetailView):
    model = Note