# Generated by Django 5.1.5 on 2025-01-19 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker_app', '0004_remove_workerprofile_skills_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerprofile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
