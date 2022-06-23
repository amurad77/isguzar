# Generated by Django 4.0.4 on 2022-06-23 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CareerCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media/creer_center', verbose_name='Logo')),
                ('title', models.CharField(max_length=50, verbose_name='Basliq')),
                ('slug', models.SlugField(editable=False, max_length=110, unique=True, verbose_name='Slug')),
                ('company', models.CharField(max_length=50, verbose_name='Şirkət')),
                ('mail', models.CharField(max_length=50, verbose_name='Mail')),
                ('adress', models.CharField(max_length=200, verbose_name='Ünvan')),
                ('views', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=50, verbose_name='Tag')),
            ],
        ),
        migrations.CreateModel(
            name='DesiredFeautures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desired_features', models.CharField(max_length=500, verbose_name='İstənilən Xüsusiyyətlər')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('career_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.careercenter')),
            ],
            options={
                'verbose_name': 'Kariyera merkezi istenilen xususiyyet',
                'verbose_name_plural': 'Kariyera merkezi istenilen xususiyyetler',
                'ordering': ('-created_at',),
            },
        ),
    ]
