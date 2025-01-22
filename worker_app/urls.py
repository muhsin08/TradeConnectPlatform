from django.urls import path
from .views import *
urlpatterns = [
    path('Workers_profile/',Workers_profile.as_view(),name="Workers_profile"),
    path('view_profile/', ViewProfile.as_view(), name='view_profile'),
    path('certificate_edit/<int:id>/',certificate_edit.as_view(),name="certificate_edit")

]