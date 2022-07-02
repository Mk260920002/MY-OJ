from atexit import register
from django.contrib import admin
from My_App.models import submissions
 
admin.site.register(submissions)