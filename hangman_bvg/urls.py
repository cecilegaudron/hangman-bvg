from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new_game/<str:list_name>', views.new_game_view, name='new_game_view'), 
    path('game_view/<str:list_name>', views.game_view, name='game_view'),  
]