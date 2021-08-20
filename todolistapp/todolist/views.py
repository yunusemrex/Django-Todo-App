from django.shortcuts import redirect, render
from .forms import TaskForm
from .models import Task


def index(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    tasks = Task.objects.all() 
    return render(request, 'pages/index.html', context={
        "task_form": form,
        "tasks": tasks
    })


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "pages/update-task.html", context={
        "task_edit_form": form
        })


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("index")
    