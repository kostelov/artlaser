from django.urls import re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.categories, name='categories'),
    re_path(r'^categories/read/$', adminapp.categories, name='categories'),
    re_path(r'^categories/create/$', adminapp.category_create, name='category'),

    re_path(r'^products/category/(?P<pk>\d+)/$', adminapp.products, name='products'),

    re_path(r'users/read/$', adminapp.users, name='users'),
]
