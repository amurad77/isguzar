# Generated by Django 4.0.4 on 2022-05-09 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Basliq')),
                ('descrtiption', models.CharField(max_length=500, verbose_name='Məzmun')),
                ('slug', models.SlugField(editable=False, max_length=110, unique=True, verbose_name='Slug')),
                ('views', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/article_images', verbose_name='Şekil')),
                ('is_published', models.BooleanField(default=True, verbose_name='is published')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
