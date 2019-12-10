from django.shortcuts import render, get_object_or_404
from contact.models import Contact

def contact_text(request):
    firstcontact = Contact.objects
    return render(request, 'contact.html')