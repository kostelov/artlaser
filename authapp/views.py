from django.shortcuts import render


def login(request):
    if request.method == 'POST':
        pass
    context = {}
    return render(request, 'authapp/login.html', context)
