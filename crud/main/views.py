from django.shortcuts import render,redirect
from django.http import HttpResponse
from main.models import Add_Task,User_Registration
from django.contrib import messages
# Create your views here.
# def index(request):
#     if request.method == "POST":
#         taskname=request.POST.get("taskname")
#         return HttpResponse(f"task:{taskname}")
#     return render(request,"home.html")

def add_task(request):
    if request.method=="POST":
        form=Add_Task(request.POST)
        task_name=request.POST.get('')
        # user_id=
        print(request.POST)
        task=Add_Task.objects.create(
            task_name=task_name
            
        )
        form.save()
        messages.success(request,"task is added successfully")
        return redirect("")
    return render(request,"home.html")