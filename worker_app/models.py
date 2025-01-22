from django.db import models
from main_app.models import *


class WorkerProfile(models.Model):
    user = models.OneToOneField(LoginDetails, on_delete=models.CASCADE)  # Linked to Django's User model
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    phone = models.IntegerField( blank=True,null=True)
    address = models.TextField(blank=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=200,null=True,blank=True)  # Skills the worker has
    experience = models.TextField(blank=True)  # Experience the worker has
    profile_picture = models.ImageField(upload_to='upload_image/', blank=True, null=True)
    certificates=models.FileField(blank=True,null=True,upload_to='certificate/')
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    # Profile picture (optional)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # Optionally you can add more methods or properties if needed, e.g.:
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
