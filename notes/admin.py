from django.contrib import admin
from mdeditor.widgets import MDEditorWidget

from .models import Note
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    
admin.site.register(Note, NoteAdmin)