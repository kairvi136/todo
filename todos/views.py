from django.http import HttpResponse
from django.shortcuts import render
from .models import Task

def addTask(request):
    task = request.post['task']
    Task.ojects.create(task=task)
    return HttpResponse('the form is submitted')
