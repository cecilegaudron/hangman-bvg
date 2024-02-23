from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('execute/', views.game_u1, name='game_u1'),
]