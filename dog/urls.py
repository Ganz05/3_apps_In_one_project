from django.urls import path
from dog.views import *
name='dog'

urlpatterns=[
    path('dog',dog,name='dog')
]