from django.contrib import admin
from django.urls import path
import re
from . import views
urlpatterns = [
    path('', views.index),
]
