from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils.text import slugify
# from isguzar.commons import slugify
from django.urls import reverse
from article.models import Article
from core.models import News
# Create your models here.


# User = get_user_model()


class ArticleComments(models.Model):
    # relation
    article = models.ForeignKey(Article,on_delete=models.CASCADE,db_index=True,related_name="comment")


    # information
    name = models.CharField('Ad', max_length = 20)
    mail = models.CharField('Mail', max_length = 50)
    subject = models.CharField('Subject', max_length = 256)
    message = models.CharField('Mesaj', max_length = 256)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField('is published', default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment = True)

    def __str__(self):
        return self.name





class NewsComments(models.Model):
    # relation
    news = models.ForeignKey(News,on_delete=models.CASCADE,db_index=True,related_name="comment")


    # information
    name = models.CharField('Ad', max_length = 20)
    mail = models.CharField('Mail', max_length = 50)
    subject = models.CharField('Subject', max_length = 256)
    message = models.CharField('Mesaj', max_length = 256)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField('is published', default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment = True)

    def __str__(self):
        return self.name