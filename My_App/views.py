from audioop import reverse
import http

from http.client import HTTPResponse
from django.utils import timezone
from urllib.request import HTTPRedirectHandler
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from My_App.models import submissions, Problem
import os
import filecmp
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            reverse('')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {"form": form})


def dashboard(request):
    problem_list = Problem.objects.all()
    context = {
        "problem_list": problem_list
    }
    return render(request, 'dashboard.html', context)


def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    return render(request, 'problem_detail.html', {'problem': problem})

@login_required
def submit(request, problem_id):
    flag = 0
    f = 0
    try:
        os.remove(
            r'C:\Users\hpw\Downloads\Code_India\MY-OJ\My_App\My_database\solution.cpp')
    except Exception as err:
        print("Solution file does not exist")
    try:
        os.remove(
            r'C:\Users\hpw\Downloads\Code_India\MY-OJ\My_App\My_database\output.txt')
    except Exception as err:
        print("Output file does not exist")

    if(len(request.POST["code"])):
        f = request.POST["code"]

        flag = 1
    else:
        f = request.FILES["solution"]

    if (flag == 0):
        with open(r'C:\Users\hpw\Downloads\Code_India\MY-OJ\My_App\My_database\solution.cpp', 'wb+') as dest:
            for chunk in f.chunks():
                dest.write(chunk)

    else:
        with open(r'C:\Users\hpw\Downloads\Code_India\MY-OJ\My_App\My_database\solution.cpp', 'w') as dest:

            dest.write(f)

    try:
        os.remove("a.exe")
    except Exception as err:
        print("a.exe doesn't exist")
    os.system(
        r'g++ C:\Users\hpw\Downloads\Code_India\MY-OJ\My_App\My_database\solution.cpp')
    os.system(r'a.exe < C:\Users\hpw\Downloads\Code_India\MY-OJ\My_App\My_database\input.txt > C:\Users\hpw\Downloads\Code_India\MY-OJ\My_App\My_database\output.txt')

    out1 = r'C:\Users\hpw\Downloads\Code_India\MY-OJ\My_App\My_database\output.txt'
    out2 = r'C:\Users\hpw\Downloads\Code_India\MY-OJ\My_App\My_database\actualOutput.txt'

    if (filecmp.cmp(out1, out2, shallow=False)):
        verdict = "Accepted"
    else:
        verdict = "Wrong Answer"
    
    if(len(out1)==0): verdict="compilation error"
    solution = submissions()
    solution.problem = get_object_or_404(Problem, pk=problem_id)
    solution.Verdict = verdict
    solution.user=request.user
   
    solution.submitted_at = timezone.now()
    solution.submitted_code = r'C:\Users\hpw\Downloads\Code_India\MY-OJ\My_App\My_database\solution.cpp'
    solution.save()
    return HttpResponse(verdict)
