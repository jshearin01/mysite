from django.db import models
from mdeditor.fields import MDTextField #https://developpaper.com/implementation-of-beautiful-django-markdown-rich-text-app-plug-in/
# Create your models here.

class HomePage(models.Model):
    content = MDTextField()
    objects = models.Manager()

class AboutPage(models.Model):
    content = MDTextField()
    objects = models.Manager()
