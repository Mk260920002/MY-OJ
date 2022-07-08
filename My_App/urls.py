from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('register/',views.register,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('problem/<int:problem_id>/',views.problem_detail,name='problem_detail'),
    path('problem/submit/<int:problem_id>/',views.submit,name='submit'),
]
