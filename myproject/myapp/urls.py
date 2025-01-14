from django.urls import path
from . import views

urlpatterns = [
    path('Display', views.show)
]