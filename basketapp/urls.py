from django.urls import re_path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    re_path(r'^$', basketapp.main, name='main'),
]
