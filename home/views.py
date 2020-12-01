from django.shortcuts import render
from django.views import View, generic
from .models import HomePage, AboutPage

def homePageView(request):
    homepage = HomePage.objects.all().reverse()[0]
    context = {'homepage': homepage}
    return render(request, 'pages/home.html', context)

def aboutPageView(request):
    homepage = AboutPage.objects.all().reverse()[0]
    context = {'homepage': homepage}
    return render(request, 'pages/home.html', context)