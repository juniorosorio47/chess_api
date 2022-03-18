from django.contrib import admin
from django.urls import include, path
from .views import create_piece, get_possible_movements

urlpatterns = [
    path('piece/add/', create_piece),
    path('piece/movements/', get_possible_movements),
]
