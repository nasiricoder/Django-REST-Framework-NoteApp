from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    model = Note
    list_display = ['title', 'content', 'created_at',
                    'author', 'first_name', 'last_name']
