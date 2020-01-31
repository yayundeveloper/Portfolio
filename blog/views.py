from django.shortcuts import render, get_object_or_404
from blog.models import Blog

def blog_page(request):
    firstblog = Blog.objects
    return render(request, 'blog.html', {'firstblog': firstblog})

def blog_text(request,blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    return render(request, 'blog_text.html', {'blog': blog})
