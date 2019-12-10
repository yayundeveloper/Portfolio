from django.shortcuts import render
from gallery.models import Gallery
from contact.models import Contact

def home(request):
    firstgallery = Gallery.objects
    return render(request, 'home.html', {'firstgallery': firstgallery})

def contact_text(request):
    firstcontact = Contact.objects
    return render(request, 'contact.html',)
