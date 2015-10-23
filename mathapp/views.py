# mathapp/views.py


from django.shortcuts import render

from mathapp.forms import *


def index(request):

    form = ExampleForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        pass
    else:
        pass

    return render(request, 'ma/index.html', context)


def about(request):
    context = {}
    return render(request, 'ma/about.html', context)


