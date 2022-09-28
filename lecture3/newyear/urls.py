from django.urls import path
from . import views

urlpatterns = [
 
    path("", views.index, name="index"), #1arg = what is the url, them the name of the ciew func
]