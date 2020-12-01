from django.urls import path, reverse_lazy
from .views import BlogListView, BlogDetailView


app_name = 'blog'

urlpatterns = [
    path('',BlogListView.as_view(),name='all'),
    path('<slug:slug>',BlogDetailView.as_view(),name='detail')
]
