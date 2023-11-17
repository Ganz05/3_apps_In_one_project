from django.urls import path
from cat.views import *
name='cat'

urlpatterns=[
    path('cat',cat,name='cat')
]