from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Add_Task, User_Registration
from django.contrib import messages

# Create your views here.


# this function checks whether user have enter value in input box or not
def value_check(value):
    return value is None or value == ''


# this function checks user have register or not
def user_check(username, password):
    get_user = User_Registration.objects.filter(
        username=username, password=password).first()
    return get_user


# this function checks username already exist or not
def already_exist(value):
    user = User_Registration.objects.filter(username__contains=value)
    return user


# this function registers new user
def new_user_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if value_check(username):
            messages.warning(request, "please enter the username")
            return redirect("/")

        if value_check(password):
            messages.warning(request, "please enter the password")
            return redirect("/")
        print(request.POST)

        if already_exist(username):
            messages.warning(request, "please enter the different username")
            return redirect("/")
        else:
            User_Registration.objects.create(username=username,
                                             password=password)
            messages.success(request, "user registered successfully")
            return redirect("/")
    return render(request, "signup.html")


# this function checks user have register or not
def login_check(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if value_check(username):
            messages.warning(request, "please enter the username")
            return redirect("/login/")

        if value_check(password):
            messages.warning(request, "please enter the password")
            return redirect("/login/")
        user = user_check(username, password)
        print(user)
        if not user:
            messages.warning(request, "user not registered")
            return redirect("/login/")
        else:
            request.session['user_id'] = user.id
            messages.success(request, "login successful!")
            return redirect("/add-task/")
    return render(request, "signin.html")


# this function adds the tasks and display all the task on screen
def add_task(request):
    id = request.session.get('user_id')
    if not id:
        messages.error(request, "user id not found. login again")
        return redirect("/login/")

    user = User_Registration.objects.filter(id=id).first()
    if not user:
        messages.error(request, "user  not found. login again")
        return redirect("/login/")

    if request.method == "POST":
        task_name = request.POST.get('taskname')
        if value_check(task_name):
            messages.warning(request, "task cannot be empty")
        else:
            Add_Task.objects.create(
                task_name=task_name,
                user=user)
            messages.success(request, "task added successfully")
            return redirect("/add-task/")
    all_tasks = Add_Task.objects.filter(user=user).all()
    print(all_tasks)
    context = {"all_tasks": all_tasks, "user": user.username}
    return render(request, "home.html", context)


# this function mark the tasks as true when task is completed
def task_done(request, task_id):
    id = request.session.get('user_id')
    if not id:
        messages.error(request, "user id not found. login again")
        return redirect("/login/")
    task = Add_Task.objects.filter(user_id=id, id=task_id).first()
    task.task_done = 1
    task.save()
    messages.success(request, "task marked successfully")
    return redirect("/add-task/")


# this function delete the specific tasks as true when task is deleted
def delete_task(request, task_id):
    id = request.session.get('user_id')
    if not id:
        messages.error(request, "user id not found! login again")
        return redirect("/login/")
    Add_Task.objects.filter(user_id=id, id=task_id).delete()
    messages.success(request, "task deleted successfully")
    return redirect("/add-task/")


# this function redirect to login page
def logout(request):
    request.session.flush()
    return redirect('/login/')
