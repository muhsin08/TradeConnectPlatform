# Generated by Django 5.1.5 on 2025-01-18 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker_app', '0002_workerprofile_created_at_workerprofile_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workerprofile',
            name='email',
        ),
    ]
