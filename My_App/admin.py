# from atexit import register
from django.contrib import admin
from .models import Problem,testcase,submissions
 
admin.site.register(Problem)
admin.site.register(submissions)
admin.site.register(testcase)
