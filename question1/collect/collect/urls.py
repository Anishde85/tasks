from django.contrib import admin
from django.urls import path, include
from collectapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("collectapp.urls")),
]