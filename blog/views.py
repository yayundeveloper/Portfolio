from django.shortcuts import render
from blog.models import Blog

def blog_page(request):
    firstblog = Blog.objects
    return render(request, 'blog.html', {'firstblog': firstblog})