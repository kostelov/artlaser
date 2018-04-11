from django import template

register = template.Library()

URL_PREFIX = '/media/'


# @register.filter(name='default_image')
@register.filter
def default_image(string):
    if not string:
        string = 'products_image/no_image.png'

    new_string = f'{URL_PREFIX}{string}'
    return new_string


@register.filter
def default_avatar(string):
    if not string:
        string = 'users_avatars/gravatar.png'

    new_string = f'{URL_PREFIX}{string}'
    return new_string
