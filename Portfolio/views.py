from django.shortcuts import render
from gallery.models import Gallery

def home(request):
    firstgallery = Gallery.objects
    return render(request, 'home.html', {'firstgallery': firstgallery})
