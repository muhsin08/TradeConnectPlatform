from django.urls import path
from .views import *
app_name='main_app'
urlpatterns = [
    path('', login_pages.as_view(), name='login'),
    path('manager/', manager_home_load.as_view(), name="loadmanager"),
    path('worker/', worker_home_load.as_view(), name='loadworker'),
    path('user/', user_home_load.as_view(), name='loaduser'),

]