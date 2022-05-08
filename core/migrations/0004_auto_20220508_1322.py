# Generated by Django 2.2.16 on 2022-05-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_articles_id_alter_articles_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(editable=False, max_length=110, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
