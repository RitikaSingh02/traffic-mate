from django.urls import path , include
from .views import directions, location , home, main
urlpatterns = [
    path('home' , home),
    path('location' , location),
    path('main/<str:pick>/<str:drop>' , main),
    path('directions' , directions),
]
