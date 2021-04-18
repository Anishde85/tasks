from django.urls import path
from collectapp.views import hero_list
urlpatterns = [
    path("",hero_list,name="hero_list"),
]