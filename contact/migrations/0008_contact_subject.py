# Generated by Django 4.0.5 on 2022-07-01 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_remove_contact_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=1, max_length=150, verbose_name='Ne haqda'),
            preserve_default=False,
        ),
    ]
