from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('add_movie/', views.add_movie, name='add_movie')
]