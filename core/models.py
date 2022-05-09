from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils.text import slugify
# from isguzar.commons import slugify
from django.urls import reverse
from article.models import *

# Create your models here.


User = get_user_model()



class News(models.Model):
    # relation
    owner =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')

    # information
    title = models.CharField('Basliq', max_length = 50)
    descrtiption = models.CharField('Məzmun', max_length = 500)
    slug = models.SlugField('Slug', max_length = 110, unique = True, editable = False)
    views = models.PositiveIntegerField(default = 0)
    image = models.ImageField("Şekil", upload_to = 'media/news_images', null=True, blank=True)

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



# class Comments(models.Model):
#     # relation
#     news = models.ForeignKey(News,on_delete=models.CASCADE,db_index=True,related_name="comment")


#     # information
#     name = models.CharField('Ad', max_length = 20)
#     mail = models.CharField('Mail', max_length = 50)
#     subject = models.CharField('Subject', max_length = 256)
#     message = models.CharField('Mesaj', max_length = 256)

#     # moderations
#     created_at = models.DateTimeField(auto_now_add=True)
#     approved_comment = models.BooleanField('is published', default=False)


#     def approve(self):
#         self.approved_comment = True
#         self.save()

#     def approved_comments(self):
#         return self.comments.filter(approved_comment = True)

#     def __str__(self):
#         return self.name