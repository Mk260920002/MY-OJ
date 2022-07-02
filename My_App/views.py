from re import A
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import  render, redirect

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
    return render(request,'dashboard.html') 


