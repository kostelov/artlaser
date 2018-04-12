from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.models import ShopUser
from authapp.forms import ShopUserRegisterForm
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda user: user.is_superuser)
def categories(request):
    title = 'Категории'

    categories_list = ProductCategory.objects.all().order_by('-is_active', 'name')

    context = {
        'title': title,
        'objects': categories_list,
    }

    return render(request, 'adminapp/categories.html', context)


# @user_passes_test(lambda user: user.is_superuser)
# def category_create(request):
#     title = 'Новая категория'
#     form = ProductCategoryEditForm()
#     if request.method == 'POST':
#         form = ProductCategoryEditForm(request.POST)
#         # Получаем данные и проверяем есть ли они в request
#         if form.is_valid():
#             try:
#                 form.save()
#                 # После сохранения данных возвращаемся к списку пользователей
#                 return HttpResponseRedirect(reverse('administrator:categories'))
#             except ValueError:
#                 pass
#
#     context = {
#         'title': title,
#         'form': form,
#     }
#     return render(request, 'adminapp/category_edit.html', context)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_edit.html'
    success_url = reverse_lazy('administrator:categories')
    # fields = ('__all__')
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda user: user.is_superuser)
# def category_update(request, pk):
#     title = 'Редактирование категории'
#
#     category = get_object_or_404(ProductCategory, pk=int(pk))
#     form = ProductCategoryEditForm(instance=category)
#     if request.method == 'POST':
#         form = ProductCategoryEditForm(request.POST, instance=category)
#         # Получаем данные и проверяем есть ли они в request
#         if form.is_valid():
#             try:
#                 form.save()
#                 # После сохранения данных возвращаемся к списку пользователей
#                 return HttpResponseRedirect(reverse('administrator:categories'))
#             except ValueError:
#                 pass
#         else:
#             form = ProductCategoryEditForm(instance=object)
#
#     context = {
#         'title': title,
#         'form': form,
#     }
#     return render(request, 'adminapp/category_edit.html', context)


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_edit.html'
    success_url = reverse_lazy('administrator:categories')
    form_class = ProductCategoryEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование категории'
        return context

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@user_passes_test(lambda user: user.is_superuser)
def category_del(request, pk):
    category = get_object_or_404(ProductCategory, pk=int(pk))
    if category:
        category.is_active = False
        category.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# class ProductCategoryDeleteView(DeleteView):
#     model = ProductCategory
#     template_name = # нужен отдельно шаблон
#     success_url = reverse_lazy('administrator:categories')
#
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.is_active = False
#         self.object.save()
#         return HttpResponseRedirect(self.success_url())


@user_passes_test(lambda user: user.is_superuser)
def category_activate(request, pk):
    category = get_object_or_404(ProductCategory, pk=int(pk))
    if category:
        category.is_active = True
        category.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# @user_passes_test(lambda user: user.is_superuser)
# def users(request):
#     title = 'Пользователи'
#     users_list = ShopUser.objects.all().order_by('-is_active', 'username')
#
#     context = {
#         'title': title,
#         'objects': users_list,
#     }
#
#     return render(request, 'adminapp/users.html', context)


class UserListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователи'
        return context

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@user_passes_test(lambda user: user.is_superuser)
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


@user_passes_test(lambda user: user.is_superuser)
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
            'object': user,
        }
        return render(request, 'adminapp/user_edit.html', context)


@user_passes_test(lambda user: user.is_superuser)
def user_del(request, pk):
    user = get_object_or_404(ShopUser, pk=int(pk))
    if user:
        # user.delete()
        user.is_active = False
        user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda user: user.is_superuser)
def user_activate(request, pk):
    user = get_object_or_404(ShopUser, pk=int(pk))
    if user:
        # user.delete()
        user.is_active = True
        user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda user: user.is_superuser)
def products(request, category_pk):
    title = 'Товары'

    products_list = Product.objects.filter(category__pk=category_pk).order_by('name')
    # Получим текущую категорию и передадим в шаблон, чтобы не было ошибки, если категория пустая
    category = get_object_or_404(ProductCategory, pk=int(category_pk))

    context = {
        'title': title,
        'objects': products_list,
        'category': category,
    }

    return render(request, 'adminapp/products_list.html', context)


# @user_passes_test(lambda user: user.is_superuser)
# def product_read(request, product_pk):
#     product = get_object_or_404(Product, pk=int(product_pk))
#     title = 'Подробнее'
#     context = {
#         'title': title,
#         'object': product,
#     }
#     return render(request, 'adminapp/product_detail.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_detail.html'

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


@user_passes_test(lambda user: user.is_superuser)
def product_create(request, category_pk):
    title = 'Добавить товар'
    category = get_object_or_404(ProductCategory, pk=int(category_pk))
    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administrator:products', kwargs={'category_pk': category_pk}))
    else:
        form = ProductEditForm(initial={'category': category})

    context = {
        'title': title,
        'category': category,
        'form': form,
    }

    return render(request, 'adminapp/product_edit.html', context)


@user_passes_test(lambda user: user.is_superuser)
def product_update(request, product_pk):
    title = 'Изменить товар'
    product = get_object_or_404(Product, pk=int(product_pk))
    category = product.category
    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administrator:products', kwargs={'category_pk': category.pk}))
    else:
        form = ProductEditForm(instance=product)

    context = {
        'title': title,
        'category': category,
        'form': form,
    }

    return render(request, 'adminapp/product_edit.html', context)


@user_passes_test(lambda user: user.is_superuser)
def product_del(request, product_pk):
    product = get_object_or_404(Product, pk=int(product_pk))
    if product:
        product.is_active = False
        product.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(lambda user: user.is_superuser)
def product_activate(request, product_pk):
    product = get_object_or_404(Product, pk=int(product_pk))
    if product:
        product.is_active = True
        product.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
