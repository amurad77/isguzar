from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.



class Contact(models.Model):
    # information
    name = models.CharField('Ad', max_length = 20)
    email = models.EmailField('Mail', max_length = 50)
    subject = models.CharField('Ne haqda', max_length = 150)
    messege = models.CharField('Mesaj', max_length = 1000)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




class Subscribe(models.Model):
    # information
    email = models.CharField('Mail', max_length = 50, unique=True)


    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
