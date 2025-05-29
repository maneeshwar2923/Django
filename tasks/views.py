from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'tasks/create_task.html')

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        completed = request.POST.get('completed') == 'on'
        task.title = title
        task.completed = completed
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/update_task.html', {'task': task})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete_task.html', {'task': task})

def complete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = True
    task.save()
    return redirect('task_list')
