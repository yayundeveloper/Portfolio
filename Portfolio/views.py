from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contact_text(request):
    return render(request, 'contact.html')
