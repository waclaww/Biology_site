from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Task
from Test.models import *
  
def index(request):
    context = {
        "articles": Article.objects.all(),
        "title": "Наследственность и изменчивость организмов",
    }
    return render(request, 'index.html', context)

def article(request, id):
    article = Article.objects.get(id = id)
    context = {
        "article": article,
        "title": article.title,
    }
    return render(request, 'article.html', context)



def tasks(request):
    context = {
        "tasks": Task.objects.all(),
        "title": "Задачи",
    }
    return render(request, 'tasks.html', context)



def condition(request, id):
    task = Task.objects.get(id = id)
    context = {
        "task": task,
        "title": task.title,
    }
    return render(request, 'condition.html', context)


def contacts(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')