from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Add_Task, User_Registration
from django.contrib import messages
# Create your views here.
# def index(request):
#     if request.method == "POST":
#         taskname=request.POST.get("taskname")
#         return HttpResponse(f"task:{taskname}")
#     return render(request,"home.html")

def value_check(value):
    return value is None or value is ''

def new_user_register(request):
    if request.method == "POST":
        username = request.POST.get("usename")
        password = request.POST.get("password")
        
        if value_check(username):
            messages.success(request, "please enter the username")
            return redirect("/")
        
        if value_check(password):
            messages.success(request, "please enter the password")
            return redirect("/")
        
        print(request.POST)
        user=User_Registration(username=username,
                               password=password)
        user.save()
        messages.success(request, "user register successfully")
        return redirect("/")
    return render(request, "signup.html")



def  user_check(username,password):     
        get_user=User_Registration.objects.get(username=username,password=password)
        return get_user
        
def login_check(request):
    if request.method == "POST":
        username = request.POST.get("usename")
        password = request.POST.get("password")
        user=user_check(username,password)
        if not user :
           messages.success(request, "user is not register")
           return redirect("/")
        else:
           messages.success(request, "login successful!")    
           return redirect("")
    return render(request,"signin.html")

def add_task(request):
    if request.method == "POST": 
        task_name = request.POST.get('')
        user=user_check()
        user_id=Add_Task.objects.get(user_id)
        print(request.POST)
        task = Add_Task.objects.create(
            task_name=task_name)
        task.save()
        messages.success(request, "task is added successfully")
        return redirect("")
    return render(request, "home.html")
