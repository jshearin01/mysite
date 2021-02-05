from django.db import models
from django.utils.text import slugify
from mdeditor.fields import MDTextField #https://developpaper.com/implementation-of-beautiful-django-markdown-rich-text-app-plug-in/
from django.core.validators import FileExtensionValidator
import datetime
import string
import random

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

# Create your models here.
    
#https://www.kodnito.com/posts/slugify-urls-django/


class BlogPost(models.Model):
    PUBLISHED = 'PUB'
    DRAFT = 'DRA'
    PUBLISH_CHOICES = (
        (PUBLISHED,'Publish'),
        (DRAFT,'Save as Draft')
    )
    title = models.CharField(max_length=255)
    intro = models.TextField(blank=True,null=True)
    content = MDTextField()
    image = models.ImageField(upload_to='files',blank=True,null=True)
    powerpoint = models.TextField(null=True,blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    created_time = models.DateTimeField(auto_created=True)
    published = models.CharField(
                max_length=3,
                choices=PUBLISH_CHOICES,
                default=DRAFT)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            self.slug = slugify(self.title)
            super(BlogPost, self).save(*args, **kwargs)
        except:
            if not self.slug:
                self.slug = slugify(self.title + "-" + rand_slug())
            super(BlogPost, self).save(*args, **kwargs)

    objects = models.Manager()


class Persona(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=40, null=True,blank=True)
    image = models.ImageField(upload_to='files',blank=True,null=True)
    content = MDTextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.SET_NULL, null=True, blank=True)
    objects = models.Manager()