from django.contrib import admin
from django.urls import path,include
from . import views     # . as the file is in same directory, views as from view.py file
from django.shortcuts import render

app_name="employee"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index,name='index'),
    path("album_form/",views.album_form,name='album_form'),
    path("musician_form/", views.musician_form,name='musician_form'),
    path("album_list/<int:artist_id>/", views.album_list, name='album_list'),
    #path("employee/", include('employee.urls'))  #employee project's urls.py file to include
]
