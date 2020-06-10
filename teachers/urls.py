from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.teacherHome, name='teacherHome'),
    path('log/', views.log, name='log'),
    path('studentList/', views.studentList, name='studentList'),
    path('addPost/', views.addPost, name='addPost'),
    path(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),


]
