from django.contrib import admin
from mdeditor.widgets import MDEditorWidget

from .models import BlogPost,Persona
# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Persona)