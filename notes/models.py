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


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = MDTextField()
    slug = models.SlugField(max_length=255, unique=True)
    created_time = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            self.slug = slugify(self.title)
            super(Note, self).save(*args, **kwargs)
        except:
            if not self.slug:
                self.slug = slugify(self.title + "-" + rand_slug())
            super(Note, self).save(*args, **kwargs)

    objects = models.Manager()