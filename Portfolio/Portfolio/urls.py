from django.contrib import admin
from django.urls import path
#from . import views     # . as the file is in same directory, views as from view.py file
from django.conf.urls import include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('employee.urls')),
    #path("employee/", include('employee.urls'))  #employee project's urls.py file to include
]
