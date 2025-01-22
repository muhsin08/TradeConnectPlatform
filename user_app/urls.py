from django.urls import path
from .views import *

urlpatterns = [
    path('users_profile/', users_profile.as_view(), name="users_profile"),

]