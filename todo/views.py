from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect

def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

def task_create(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    return render(request, 'todo/form.html', {'form': form})


from django.shortcuts import get_object_or_404

def task_update(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'todo/form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('index')

    return render(request, 'todo/delete.html', {'task': task})