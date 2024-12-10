from django.contrib import admin
from django.urls import path

# VIEWS
from app.views import index

#PATHS
urlpatterns = [
    path('', index)
]
