from django.db import models
from datetime import datetime
from django.urls import reverse


class CareerCenter(models.Model):
    # information
    logo = models.ImageField('Logo', upload_to = 'media/creer_center', null = True, blank = True)
    title = models.CharField('Basliq', max_length = 50)
    company = models.CharField('Şirkət', max_length = 50)
    mail = models.CharField('Mail', max_length = 50)
    adress = models.CharField('Ünvan', max_length = 200)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DesiredFeautures(models.Model):
    #relation's
    career_center = models.ForeignKey(CareerCenter, on_delete = models.CASCADE)

    desired_features = models.CharField('İstənilən Xüsusiyyətlər', max_length = 500)
    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Kariyera merkezi istenilen xususiyyet'
        verbose_name_plural = 'Kariyera merkezi istenilen xususiyyetler'
        ordering = ('-created_at',)