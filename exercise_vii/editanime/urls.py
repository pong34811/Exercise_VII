from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path ('', views.homepage),
    path ('edit/<animal_id>', views.editanimelist),

]
