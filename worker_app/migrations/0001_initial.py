# Generated by Django 5.1.5 on 2025-01-18 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WorkerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('address', models.TextField(blank=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('experience', models.TextField(blank=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='upload_image/')),
                ('skills', models.ManyToManyField(blank=True, related_name='workers', to='worker_app.skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.logindetails')),
            ],
        ),
    ]
