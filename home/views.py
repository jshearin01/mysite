from django.shortcuts import render
from django.views import View, generic
from .models import HomePage, AboutPage, Resume

def homePageView(request):
    homepage = HomePage.objects.all().reverse()[0]
    context = {'homepage': homepage}
    return render(request, 'pages/home.html', context)

def aboutPageView(request):
    aboutpage = AboutPage.objects.all().reverse()[0]
    context = {'aboutpage': aboutpage}
    return render(request, 'pages/about.html', context)

def resumePageView(request):
    resume = Resume.objects.all().reverse()[0]
    context = {'resume': resume}
    return render(request, 'pages/resume.html', context)

def handler404(request, exception):
    return render(request, 'pages/404.html', status=404)

def handler500(request):
    return render(request, 'pages/500.html', status=500)