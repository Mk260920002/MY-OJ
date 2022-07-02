
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('My_App.urls')),
  
    path('logout/',include('My_App.urls')),
    path('register/',include('My_App.urls')),
]
