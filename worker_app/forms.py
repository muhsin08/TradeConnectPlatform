from django import forms
from .models import WorkerProfile

class WorkerProfileForm(forms.ModelForm):
    class Meta:
        model = WorkerProfile
        fields = ['first_name', 'last_name', 'phone', 'address', 'bio', 'profile_picture','skills','certificates']

