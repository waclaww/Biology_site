from django.urls import path
from .views import *

urlpatterns = [
    path('login', log_in, name='login'),
    path('logout', log_out, name='logout'),
    path('registration', registration, name="registration"),
    path('<str:username>', profile, name='profile'),
    path('<str:username>/r', results, name='results'),
]