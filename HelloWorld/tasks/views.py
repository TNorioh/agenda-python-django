from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import task

def taskList(request):
    tasks = task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(task, pk=id)
    return render(request, 'tasks/tasks.html', {'task' : task})

def helloworld(request):
    return HttpResponse('Hello World')


