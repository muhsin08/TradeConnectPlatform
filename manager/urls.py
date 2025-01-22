from django.urls import path
from .views import *

urlpatterns = [
    path('verify/', Verify.as_view(), name="verify"),
    path('verification/<int:id>/', Verify.as_view(), name="verification")

]