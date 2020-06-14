from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:slug>', views.readMore, name='readMore'),
     path('search/', views.search, name='search'),
     path('contact/', views.contact, name='contact'),
    path('aboutMe/', views.aboutMe, name='aboutMe'),

]
