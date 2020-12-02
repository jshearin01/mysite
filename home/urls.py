from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from .views import homePageView, aboutPageView, resumePageView
from . import views


app_name = 'home'

urlpatterns = [
    path('',homePageView,name='home_base'),
    path('home/',homePageView,name='home_page'),
    path('about/',aboutPageView,name='about'),
    path('resume/',resumePageView,name='resume'),

]
