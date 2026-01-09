from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Result
from django.core.paginator import Paginator
from .forms import RegisterUserForm



def registration(request):
    if request.user.is_authenticated:
        messages.success(request, "Вы не можете зайти на эту страницу, так как вы уже авторизованы!")
        return redirect("home")
    else:
        if request.method == "POST":
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, "Регистрация успешно завершена!")
                return redirect("home")
        else:
            form = RegisterUserForm()
        context = {
            'form': form,
            'title': 'Регистрация',
        }    
        return render(request, 'registration.html', context)

def log_in(request):
    if request.method == "POST":
        username = request.POST.get("username", False)
        password = request.POST.get("password", False)
        if not username and not password:
            messages.success(request, "Не был указан логин или пароль!")
            return redirect("home")
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Вы вошли в аккаунт {username}")
                return redirect("home")
            else:
                messages.success(request, "Неверный логин и/или пароль!")
                return redirect("home")
    else:
        context = {
            
        }
        return render(request, "login.html", context)

@login_required(login_url="login")
def log_out(request):
    username = request.user
    logout(request)
    messages.success(request, "Вы успешно вышли из аккаунта!")
    return redirect("home")

@login_required(login_url="login")
def profile(request, username):
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        context = {
            "title": f"Профиль пользователя {user.username}",
            "profile": user,
            "has_results": Result.objects.filter(user__id=user.id).exists()
        }
        return render(request, "profile.html", context)
    else:
        messages.success(request, "Пользователя с таким именем пользователя не существует!")
        return redirect("home")

@login_required(login_url="login")
def results(request, username):
    if User.objects.filter(username=username).exists():
        items_on_page = 10
        user = User.objects.get(username=username)
        result = Result.objects.filter(user__id=user.id)
        pag = Paginator(result, items_on_page)
        page_number = request.GET.get('page', 1)
        page = pag.get_page(page_number)
        context = {
            "title": f"Результаты пользователя {user.username}",
            "results": page,
            "profile": user,
        }
        return render(request, "results.html", context)
    else:
        messages.success(request, "Пользователя с таким именем пользователя не существует!")
        return redirect("home")

# 1. Страница пользователя (Вывести его юзернейм, дату последнего онлайна и роль (если is_staff=True то это учитель. Иначе это ученик))
# 2. Имя пользователя в шапке
# 3. Попытаться сделать так, чтобы при пролистывании страницы пропадала зеленая шапка, а черная перемещалась бы выше и следовала за страницей.
# 4. Подключить тему в админку и настроить ее. (Django Jazzmin)