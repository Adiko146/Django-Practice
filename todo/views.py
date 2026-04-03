from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todo/index.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('index')
    else:
        form = TaskForm()

    return render(request, 'todo/form.html', {'form': form})


from django.shortcuts import get_object_or_404

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'todo/form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('index')

    return render(request, 'todo/delete.html', {'task': task})