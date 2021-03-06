from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.translation import gettext as _
# Create your models here.

WORKING_CHOICES =(
    (1, _("Sektordayam")),
    (2, _("Tələbəyəm")),
    (3, _("İşləmirəm"))
)

TIME = (
    ("1", "Həftədə 1-2 məqalə"),
    ("2", "Həftədə 3-4 məqalə"),
    ("3", "Ayda 1-2 məqalə")
)

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


# class Author(models.Model):
#     name_surname = models.CharField('Ad və Soyad',  max_length = 150)
#     mail = models.CharField('E-mail',  max_length = 150)
#     phono = models.CharField('Telefon',  max_length = 150)
#     working_status = models.CharField('Hal hazırda işləyirsiniz? (Nə?)', max_length = 150)
#     education_industry = models.CharField('Təhsil və sənayə təcrübəniz',  max_length = 150)
#     subjects = models.CharField('Hansı mövzuda yaza bilərsiniz?',  max_length = 150)
#     time = models.CharField('Nə qədər vaxtdan bir məzmun təqdim edə bilərsiniz?',  max_length = 150)


class Author(models.Model):
    # information
    name = models.CharField('Ad və Soyad', max_length = 150)
    email = models.EmailField('E-mail', max_length = 150)
    phone = models.CharField('Telefon',  max_length = 150)
    working_status = models.CharField('Hal hazırda işləyirsiniz? (Nə?)', max_length = 150)
    education_industry = models.CharField('Təhsil və sənayə təcrübəniz',  max_length = 150)
    subjects = models.CharField('Hansı mövzuda yaza bilərsiniz?',  max_length = 150)
    time = models.CharField('Nə qədər vaxtdan bir məzmun təqdim edə bilərsiniz?', blank = True, null = True, max_length = 150)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name