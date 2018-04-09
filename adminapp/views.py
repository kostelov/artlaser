from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.contrib import auth
from adminapp.forms import ShopUserAdminEditForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from authapp.forms import ShopUserRegisterForm


def categories(request):
    title = 'Категории'

    categories_list = ProductCategory.objects.all()

    context = {
        'title': title,
        'objects': categories_list,
    }

    return render(request, 'adminapp/categories.html', context)


def category_update(request):
    pass


def category_del(request):
    pass


def category_create(request):
    pass


def users(request):
    title = 'Пользователи'
    users_list = ShopUser.objects.all().order_by('-is_active', 'username')

    context = {
        'title': title,
        'objects': users_list,
    }

    return render(request, 'adminapp/users.html', context)


def user_create(request):
    title = 'Регистрация пользователя'
    form = ShopUserRegisterForm()
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        # Получаем данные и проверяем есть ли они в request
        if form.is_valid():
            try:
                form.save()
                # После сохранения данных возвращаемся к списку пользователей
                return HttpResponseRedirect(reverse('administrator:users'))
            except ValueError:
                pass

    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'adminapp/user_edit.html', context)


def user_update(request, pk):
    title = 'Редактирование профиля'
    user = get_object_or_404(ShopUser, pk=int(pk))
    if user:
        if request.method == 'POST':
            form = ShopUserAdminEditForm(request.POST, request.FILES, instance=user)
            # Получаем данные и проверяем есть ли они в request
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('administrator:users'))
        else:
            form = ShopUserAdminEditForm(instance=user)

        context = {
            'title': title,
            'form': form,
        }
        return render(request, 'adminapp/user_edit.html', context)


def user_del(request, pk):
    user = get_object_or_404(ShopUser, pk=int(pk))
    if user:
        # user.delete()
        user.is_active = False
        user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def user_activate(request, pk):
    user = get_object_or_404(ShopUser, pk=int(pk))
    if user:
        # user.delete()
        user.is_active = True
        user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def products(request, pk):
    title = 'Товары'

    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'objects': products_list,
    }

    return render(request, 'adminapp/products_list.html', context)
