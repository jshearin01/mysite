from django.urls import path, reverse_lazy
from .views import NoteDetailView, NoteListView


app_name = 'notes'

urlpatterns = [
    path('',NoteListView.as_view(),name='all'),
    path('<slug:slug>',NoteDetailView.as_view(),name='detail')
]