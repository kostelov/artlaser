from django.urls import re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.categories, name='categories'),
    re_path(r'^categories/$', adminapp.categories, name='categories'),
    re_path(r'^categories/create/$', adminapp.category_create, name='category'),

    re_path(r'^products/category/(?P<pk>\d+)/$', adminapp.products, name='products'),

    re_path(r'^users/$', adminapp.users, name='users'),
    re_path(r'^users/create/$', adminapp.user_create, name='user_create'),
    re_path(r'^users/update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    re_path(r'^users/delete/(?P<pk>\d+)/$', adminapp.user_del, name='user_del'),
    re_path(r'^users/activate/(?P<pk>\d+)/$', adminapp.user_activate, name='user_activate'),
]
