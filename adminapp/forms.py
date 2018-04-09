import re
from django import forms
from mainapp.models import ProductCategory
from authapp.models import ShopUser
from authapp.forms import ShopUserEditForm


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = ('is_active', 'username', 'first_name', 'last_name', 'email', 'phone', 'age', 'avatar', 'password')


class ProductCategoryEditForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''