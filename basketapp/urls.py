from django.urls import re_path
import basketapp.views as basketapp


app_name = 'basketapp'

urlpatterns = [
    re_path(r'^$', basketapp.main_basket, name='main_basket'),
    re_path(r'^product/add/(\d+)$', basketapp.product_add, name='product_add'),
    re_path(r'^product/del/(\d+)$', basketapp.product_del, name='product_del'),
    re_path(r'^product/edit/(?P<pk>\d+)/(?P<quantity>\d+)/$', basketapp.product_edit),
]
