# Generated by Django 4.0.5 on 2022-06-30 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_detail_image2_news_detail_image3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='video_link',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
