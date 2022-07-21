from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify
from tinymce import models as tinymce_models
from django.contrib.auth import get_user_model



User = get_user_model()


class UserProfile(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='news')
    name_surname = models.CharField('Ad və Soyad', max_length = 256)
    image = models.ImageField("Şekil", upload_to = 'media/admin_image', null=True, blank=True)
    work = models.CharField('İş', max_length = 256)
    linkedin = models.CharField('Linkedin', max_length = 256, null=True, blank=True)
    twitter = models.CharField('Twitter', max_length = 256, null=True, blank=True)
    facebook = models.CharField('Facebook', max_length = 256, null=True, blank=True)



    def __str__(self):
        return self.name_surname



class ArticleTags(models.Model):
    tags = models.CharField('Tag', max_length = 50)

    def __str__(self):
        return self.tags


class NewsTags(models.Model):
    tags = models.CharField('Tag', max_length = 50)

    def __str__(self):
        return self.tags


class CareerCenterCategory(models.Model):
    title = models.CharField('Elanın kateqoriyası', max_length = 50)

    def __str__(self):
        return self.title

class CareerCenter(models.Model):
    #relation's
    category = models.ForeignKey(CareerCenterCategory, on_delete = models.CASCADE)

    # information
    logo = models.ImageField('Logo', upload_to = 'media/creer_center', null = True, blank = True)
    descrtiption = tinymce_models.HTMLField('Məzmun', max_length = 15000)
    title = models.CharField('Basliq', max_length = 50)
    slug = models.SlugField('Slug', max_length = 110, unique = True, editable = False)
    company = models.CharField('Şirkət', max_length = 50)
    mail = models.CharField('Mail', max_length = 50)
    adress = models.CharField('Ünvan', max_length = 200)
    views = models.PositiveIntegerField(default = 0)


    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('career_center_detail', kwargs = {'slug': self.slug})

    def get_uniqe_slug(self):
        slug = slugify(self.title.replace('ə', 'e'))
        unique_slug = slug
        counter = 1
        while CareerCenter.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_uniqe_slug()
        return super(CareerCenter, self).save(*args, **kwargs)

