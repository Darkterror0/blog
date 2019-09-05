from django.contrib import admin
from django.urls import path

from django.urls import path
from . import views

app_name='guanwang'

urlpatterns = [
    path('',views.index),
]
