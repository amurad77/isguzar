from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils.text import slugify
# from isguzar.commons import slugify
from django.urls import reverse
from article.models import *
from core.models import NewsTags, UserProfile


from tinymce import models as tinymce_models
# Create your models here.


class News(models.Model):
    # relation
    owner =  models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name='news')
    tags = models.ForeignKey(NewsTags, on_delete = models.CASCADE)

    # information
    detail_image = models.ImageField("Şekil", upload_to = 'media/news_images', null=True, blank=True)
    detail_image2 = models.ImageField("Şekil", upload_to = 'media/news_images', null=True, blank=True)
    detail_image3 = models.ImageField("Şekil", upload_to = 'media/news_images', null=True, blank=True)
    detail_image4 = models.ImageField("Şekil", upload_to = 'media/news_images', null=True, blank=True)
    detail_image5 = models.ImageField("Şekil", upload_to = 'media/news_images', null=True, blank=True)
    detail_image6 = models.ImageField("Şekil", upload_to = 'media/news_images', null=True, blank=True)
    title = models.CharField('Basliq', max_length = 250)
    descrtiption_block = tinymce_models.HTMLField('Məzmun blok', max_length = 5000, null=True, blank=True)
    descrtiption = tinymce_models.HTMLField('Məzmun', max_length = 5000, null=True, blank=True)
    descrtiption2 = tinymce_models.HTMLField('Məzmun', max_length = 5000, null=True, blank=True)
    descrtiption3 = tinymce_models.HTMLField('Məzmun', max_length = 5000, null=True, blank=True)
    descrtiption4 = tinymce_models.HTMLField('Məzmun', max_length = 5000, null=True, blank=True)
    descrtiption5 = tinymce_models.HTMLField('Məzmun', max_length = 5000, null=True, blank=True)
    descrtiption6 = tinymce_models.HTMLField('Məzmun', max_length = 5000, null=True, blank=True)

    slug = models.SlugField('Slug', max_length = 110, unique = True, editable = False)
    views = models.PositiveIntegerField(default = 0)
    image = models.ImageField("Şekil", upload_to = 'media/news_images', null=True, blank=True)
    time = models.PositiveIntegerField('Neçə dəqiqəlik xəbər', default = 0)
    video_link = models.URLField(max_length=300, blank=True, null=True)
    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_news', kwargs = {'slug': self.slug})

    def get_uniqe_slug(self):
        slug = slugify(self.title.replace('ə', 'e'))
        unique_slug = slug
        counter = 1
        while News.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_uniqe_slug()
        return super(News, self).save(*args, **kwargs)

    # def add_view_count(self):
    #     self.views +=3
    #     self.save()
    #     return True
