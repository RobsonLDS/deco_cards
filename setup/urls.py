from django.urls import path

# VIEWS
from app.views.views import index

#PATHS
urlpatterns = [
    path('', index)
]
