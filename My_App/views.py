import http
from http.client import HTTPResponse
from urllib.request import HTTPRedirectHandler
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import  render, redirect
from My_App.models import submissions,Problem
def index(request):
    return HttpResponse("This is homepage")
def register(request):
  if request.method=='POST':
      form=UserCreationForm(request.POST)
      if form.is_valid():
          form.save()
          redirect('')
  else:form=UserCreationForm()

  return render(request,'register.html',{"form":form})

def dashboard(request):
    problem_list=Problem.objects.all()
    context={
        "problem_list":problem_list
    }
    return render(request,'dashboard.html',context) 


def problem_detail(request,problem_id):
    problem=get_object_or_404(Problem,pk=problem_id)
    return render(request,'problem_detail.html',{'problem':problem})

def submit(request,problem_id):
    return HttpResponse("hii how are you")

