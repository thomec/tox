# mathapp/views.py


from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'ma/index.html', context)


def about(request):
    context = {}
    return render(request, 'ma/about.html', context)


