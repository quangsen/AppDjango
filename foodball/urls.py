from django.urls import path
from . import views

urlpatterns = [
    path('', views.foodball_index, name='foodball_index'),
]
