from django.urls import path
from goat.views import *
name='goat'



urlpatterns=[
    path('goat',goat,name='goat')
]