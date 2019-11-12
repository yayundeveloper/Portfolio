from django.contrib import admin
from .models import Gallery

@admin.register(Gallery)
class Gallery(admin.ModelAdmin):
    list_display = ('title', 'description')