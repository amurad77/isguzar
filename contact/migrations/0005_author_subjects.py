# Generated by Django 4.0.5 on 2022-06-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_author_education_industry'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='subjects',
            field=models.CharField(default=1, max_length=150, verbose_name='Hansı mövzuda yaza bilərsiniz?'),
            preserve_default=False,
        ),
    ]
