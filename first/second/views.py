from django.shortcuts import render, redirect
from .models import Category, SubTask
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


@login_required()

    
def getTodo(request):
    if request.method == "GET":
        userData = request.user
        Alldata = Category.objects.filter(user=userData)
        context = {"items": Alldata}
        return render(request, "index.html", context)


@login_required()
def addTodo(request):
    if request.method == "POST":
        data = request.POST["test"]
        user_data = request.user
        Category.objects.create(name=data, user=user_data)

    Alldata = Category.objects.filter(user=request.user)
    context = {"items": Alldata}

    return render(request, "index.html", context)


@login_required()
def delete(request, todo_id):
    task = Category.objects.get(pk=todo_id)
    task.delete()
    return redirect("/")


@login_required()
def editTask(request, todo_id):
    edittask = Category.objects.get(pk=todo_id)
    if request.method == "POST":
        data = request.POST["edit"]
        edittask.name = data
        edittask.save()
        return redirect("getTodo")


@login_required()
def view_subtasks(request, todo_id):
    task = Category.objects.get(pk=todo_id)
    subtasks = task.subtasks.all()
    return render(request, "subtasks.html", {"task": task, "subtasks": subtasks})


@login_required()
def add_subtask(request, todo_id):
    if request.method == "POST":
        subtask_name = request.POST.get("subtask_name")
        task = Category.objects.get(pk=todo_id)
        subtask = SubTask.objects.create(name=subtask_name, task=task)
        task.subtasks.add(subtask)
        task.save()
    return redirect("view_subtasks", todo_id=todo_id)


@login_required()
def delete_subtask(request, todo_id, subtask_id):
    subtask = SubTask.objects.get(pk=subtask_id)
    subtask.delete()
    return redirect("view_subtasks", todo_id=todo_id)


@login_required()
def update_subtask(request, todo_id, subtask_id):
    if request.method == "POST":
        updated_subtask_name = request.POST.get("updated_subtask")
        subtask = SubTask.objects.get(pk=subtask_id)
        subtask.name = updated_subtask_name
        subtask.save()
    return redirect("view_subtasks", todo_id=todo_id)


def register(request):
    form = RegisterForm()
    context = {"form": form}
    if request.method == "POST":
        RegisterUser = RegisterForm(request.POST)
        if RegisterUser.is_valid():
            user = RegisterUser.save()
            print(user)
            login(request, user)
            return redirect("login")
    return render(request, "register.html", context)


def Login(request):
    form = AuthenticationForm()
    context = {"loginForm": form}
    if request.method == "POST":
        LoginUser = AuthenticationForm(request, request.POST)
        if LoginUser.is_valid():
            login(request, LoginUser.get_user())
            return redirect("/")
    return render(request, "login.html", context)
