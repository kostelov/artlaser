from django.urls import re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^categories/read/$', adminapp.categories, name='categories'),
    re_path(r'users/read/$', adminapp.users, name='users'),
]
