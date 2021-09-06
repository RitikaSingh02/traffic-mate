from django.urls import path , include
from .views import directions, get_coordinates, get_weather, location , home, main
urlpatterns = [
    path('home' , home),
    path('location' , location),
    path('main/<str:pick>/<str:drop>' , main),
    path('directions' , directions),
    path('get_coordinates' , get_coordinates),
    path('get_weather' , get_weather),


]
