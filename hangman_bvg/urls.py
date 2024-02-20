from django.urls import path
from . import views

urlpatterns = [
        # URL for list with trackings
    path('', views.index, name="index"),
]