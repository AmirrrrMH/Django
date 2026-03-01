from django.db import models


class Contact(models.Model):
    name = models.CharField(null=True,max_length=255)
    email = models.EmailField()
    subject = models.CharField(null=True,max_length=255)
    text = models.CharField(null=True,max_length=255)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)