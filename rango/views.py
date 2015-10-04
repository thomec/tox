# rango/views.py


from datetime import datetime

from django.shortcuts import (
        render, get_object_or_404, get_list_or_404, redirect
)
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from rango.bing_search import run_query



def index(request):
    # populate the context dict with categories and pages
    context = {}
    context['categories'] = Category.objects.order_by('-likes')
    context['pages'] = Page.objects.order_by('-views')

    # read the number of visits from server side cookie or set it to 1
    visits = request.session.get('visits')
    if not visits:
        visits = 1
    update_last_visit = False

    # count the visit if last_visit time doesn't exist or is older than a day
    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).days > 0:
            visits += 1
            update_last_visit = True
    else:
        update_last_visit = True

    # put the visits into context dict
    context['visits'] = visits
    context['last_visit'] = last_visit

    # update the timestamp if visit was counted
    if update_last_visit:
        request.session['visits'] = visits
        request.session['last_visit'] = str(datetime.now())
        
    return render(request, 'rango/index.html', context)



def about(request):
    visits = request.session.get('visits') or 0
    print(type(visits))
    context = {'visits': visits}
    return render(request, 'rango/about.html', context)



def category(request, slug):

    category = get_object_or_404(Category, slug=slug)    
    pages = Page.objects.filter(category=category)
    results = []
    context = {'category': category, 'pages': pages}

    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            results = run_query(query)
            context['results'] = results
    return render(request, 'rango/category.html', context)



@login_required
def add_category(request):

    # read the form data if we have a POST request
    form = CategoryForm(request.POST or None)
    context = {'form': form,}

    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect(reverse('rango:index'))
    else:
        print(form.errors)

    return render(request, 'rango/add_category.html', context)



@login_required
def add_page(request, slug):

    category = get_object_or_404(Category, slug=slug)
    form = PageForm(request.POST or None)
    context = {'category': category, 'form': form}

    if form.is_valid():

        page = form.save(commit=False)
        page.category = category
        page.views = 0
        page.save()

        return HttpResponseRedirect(reverse('rango:category', args=(slug,)))

    else:
        print(form.errors)

    return render(request, 'rango/add_page.html', context)



def search(request):

    results = []

    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            print(str(query))
            results = run_query(query)
            print(results)

    return render(request, 'rango/search.html', {'results': results})



def track(request, page):

    page = get_object_or_404(Page, id=page)
    page.views += 1
    page.save()

    return redirect(page.url)



def add_profile(request, ):
    return render(request, 'rango/add_profile.html')




def profile(request, ):
    return render(request, 'rango/profile.html')

