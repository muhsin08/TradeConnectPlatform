from django.db import models
from main_app.models import *


class Profile(models.Model):
    user = models.OneToOneField(LoginDetails, on_delete=models.CASCADE)  # Linked to Django's User model
    bio = models.TextField(blank=True)
    full_name=models.CharField(max_length=30,null=True,blank=True)
    profile_picture = models.ImageField(upload_to='upload_image/', blank=True, null=True)
    status = models.CharField(default="Active", max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.user.username
