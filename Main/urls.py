from django.urls import path
from .views import *

urlpatterns=[
    path('', index, name='home'),
    path('tasks/', tasks, name='tasks'),
    path('article/<int:id>', article, name='article'),
    path('condition/<int:id>', condition, name='condition'),
    path('contacts', contacts, name='contacts'),
    path('about', about, name='about'),
]