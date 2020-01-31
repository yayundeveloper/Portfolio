from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('title', 'date', 'image', 'text')
