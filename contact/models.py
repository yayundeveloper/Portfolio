from django.db import models

class Contact(models.Model):
    text = models.TextField(default='正文')