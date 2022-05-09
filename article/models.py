from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils.text import slugify
# from isguzar.commons import slugify
from django.urls import reverse
# from core.models import *


User = get_user_model()



class Article(models.Model):
    # relation
    owner =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')

    # information
    title = models.CharField('Basliq', max_length = 50)
    descrtiption = models.CharField('Məzmun', max_length = 500)
    slug = models.SlugField('Slug', max_length = 110, unique = True, editable = False)
    views = models.PositiveIntegerField(default = 0)
    image = models.ImageField("Şekil", upload_to = 'media/article_images', null=True, blank=True)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs = {'slug': self.slug})

    def get_uniqe_slug(self):
        slug = slugify(self.title.replace('ə', 'e'))
        unique_slug = slug
        counter = 1
        while Article.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_uniqe_slug()
        return super(Article, self).save(*args, **kwargs)

    # def add_view_count(self):
    #     self.views +=3
    #     self.save()
    #     return True