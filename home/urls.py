from django.urls import path, include
from . views import index, about

urlpatterns = [
    path("",index , name='Home'),    
    path("about/",about , name='AboutUs'),
]