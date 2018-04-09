from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm


def login(request):
    title = 'Вход'
    form = ShopUserLoginForm()
    next = request.GET['next'] if 'next' in request.GET.keys() else ''
    # Проверяем, что данные пришли методом POST
    if request.method == 'POST':
        # Получаем данные и проверяем есть ли они в request
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            # Проверяем существует ли пользователь и то что он активен
            if user and user.is_active:
                # Авторизируем пользоваетля, помещаем его в request
                auth.login(request, user)
                if 'next' in request.POST.keys():
                    # Направляем пользователя на страницу с которой пришел
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('main'))

    context = {
        'title': title,
        'login_form': form,
        'next': next,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    # Разлогиниваем пользователя
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    title = 'Регистрация'
    register_form = ShopUserRegisterForm()
    # Проверяем, что данные пришли методом POST
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        # Получаем данные и проверяем есть ли они в request
        if register_form.is_valid():
            try:
                register_form.save()
                # После сохранения данных авторизируем пользователя и направляем на главную страницу
                user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
            except ValueError:
                pass

    context = {
        'title': title,
        'register_form': register_form,
    }
    return render(request, 'authapp/register.html', context)


def edit(request):
    title = 'Мой профиль'
    edit_form = ShopUserEditForm(instance=request.user)
    # Проверяем, что данные пришли методом POST
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        # Получаем данные и проверяем есть ли они в request
        if edit_form.is_valid():
            # Сохраняем данные и остаемся в профиле
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))

    context = {
        'title': title,
        'edit_form': edit_form,
    }
    return render(request, 'authapp/edit.html', context)
