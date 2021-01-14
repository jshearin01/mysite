from django.db import models
from mdeditor.fields import MDTextField #https://developpaper.com/implementation-of-beautiful-django-markdown-rich-text-app-plug-in/
from django.core.validators import FileExtensionValidator


# Create your models here.

class HomePage(models.Model):
    content = MDTextField()
    objects = models.Manager()

class AboutPage(models.Model):
    content = MDTextField()
    objects = models.Manager()

class Resume(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files',validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    objects = models.Manager()
