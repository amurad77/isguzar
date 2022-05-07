from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from datetime import datetime
from isguzar.commons import slugify

# Create your models here.


User = get_user_model()


class Articles(models.Model):
    # relation
    owner =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    # information
    title = models.CharField('Basliq', max_length = 50)
    descrtiption = models.CharField('Məzmun', max_length = 500)
    slug = models.SlugField('Slug', max_length=110, unique=True)
    views = models.PositiveIntegerField(default=0, blank=True, null=True)
    image = models.ImageField("Şekil", upload_to='media/article_images', null=True, blank=True)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def add_view_count(self):
        self.views +=3
        self.save()
        return True



class Comment(models.Model):
    # relation
    article = models.ForeignKey(Articles,on_delete=models.CASCADE,db_index=True,related_name="comment")

    # information
    name = models.CharField('Ad', max_length = 20)
    mail = models.CharField('Mail', max_length = 50)
    subject = models.CharField('Subject', max_length = 256)
    message = models.CharField('Mesaj', max_length = 256)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Subscribe(models.Model):
    # information
    mail = mail = models.CharField('Mail', max_length = 50)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)