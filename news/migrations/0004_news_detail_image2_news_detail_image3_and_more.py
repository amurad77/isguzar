# Generated by Django 4.0.5 on 2022-06-30 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_descrtiption2_news_descrtiption3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='detail_image2',
            field=models.ImageField(blank=True, null=True, upload_to='media/news_images', verbose_name='Şekil'),
        ),
        migrations.AddField(
            model_name='news',
            name='detail_image3',
            field=models.ImageField(blank=True, null=True, upload_to='media/news_images', verbose_name='Şekil'),
        ),
        migrations.AddField(
            model_name='news',
            name='detail_image4',
            field=models.ImageField(blank=True, null=True, upload_to='media/news_images', verbose_name='Şekil'),
        ),
        migrations.AddField(
            model_name='news',
            name='detail_image5',
            field=models.ImageField(blank=True, null=True, upload_to='media/news_images', verbose_name='Şekil'),
        ),
        migrations.AddField(
            model_name='news',
            name='detail_image6',
            field=models.ImageField(blank=True, null=True, upload_to='media/news_images', verbose_name='Şekil'),
        ),
    ]
