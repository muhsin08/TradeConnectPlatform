from django.urls import path
from .views import *
urlpatterns = [
    path('Workers_profile/',Workers_profile.as_view(),name="Workers_profile"),
    path('view_profile/', ViewProfile.as_view(), name='view_profile'),

]