from django.urls import re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.categories, name='categories'),
    re_path(r'^categories/$', adminapp.categories, name='categories'),
    # re_path(r'^categories/create/$', adminapp.category_create, name='category_create'),

    re_path(r'^categories/create/$', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),

    # re_path(r'^category/update/(?P<pk>\d+)/$', adminapp.category_update, name='category_update'),

    re_path(r'^category/update/(?P<pk>\d+)/$', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),

    re_path(r'^category/delete/(?P<pk>\d+)/$', adminapp.category_del, name='category_del'),
    # re_path(r'^category/delete/(?P<pk>\d+)/$', adminapp.ProductCategoryDeleteView.as_view(), name='category_del'),
    re_path(r'^category/activate/(?P<pk>\d+)/$', adminapp.category_activate, name='category_activate'),

    re_path(r'^products/(?P<category_pk>\d+)/$', adminapp.products, name='products'),
    re_path(r'^product/create/(?P<category_pk>\d+)/$', adminapp.product_create, name='product_create'),
    # re_path(r'^product/read/(?P<product_pk>\d+)$', adminapp.product_read, name='product_read'),

    re_path(r'^product/read/(?P<pk>\d+)$', adminapp.ProductDetailView.as_view(), name='product_read'),

    re_path(r'^product/update/(?P<product_pk>\d+)/$', adminapp.product_update, name='product_update'),
    re_path(r'^product/delete/(?P<product_pk>\d+)/$', adminapp.product_del, name='product_del'),
    re_path(r'^product/activate/(?P<product_pk>\d+)/$', adminapp.product_activate, name='product_activate'),

    # re_path(r'^users/$', adminapp.users, name='users'),
    re_path(r'^users/$', adminapp.UserListView.as_view(), name='users'),
    re_path(r'^users/create/$', adminapp.user_create, name='user_create'),
    re_path(r'^users/update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    re_path(r'^users/delete/(?P<pk>\d+)/$', adminapp.user_del, name='user_del'),
    re_path(r'^users/activate/(?P<pk>\d+)/$', adminapp.user_activate, name='user_activate'),
]
