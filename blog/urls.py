from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_page),
    path('<int:blog_pk>', views.blog_text)
]