# rango/views.py


from datetime import datetime

from django.shortcuts import (
        render, get_object_or_404, get_list_or_404, redirect
        )
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from rango.bing_search import run_query


def index(request):
    """
    index view
    """
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
    pages = Page.objects.filter(category=category).order_by('-views')
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


@login_required
def like_category(request):
    
    catid = request.GET['catid'] or None
    likes = 0

    if catid:
        cat = Category.objects.get(id=int(catid))

    if cat:
        likes = cat.likes + 1
        cat.likes =  likes
        cat.save() #

    return HttpResponse(likes)


@login_required
def auto_add_page(request):

    catid = request.method.GET['catid'] or None
    url =request.method.GET['url'] or None
    title =request.method.GET['title'] or None
    context = {}

    if catid:
        category = Category.objects.get(id=int(catid))
        page = Page.objects.get_or_create(
                    category=category, title=title, url=url)
        pages = Page.objects.filter(category=category).order_by('-views')


def get_category_list(max_results=0, starts_with=''):
    
    cat_list = []

    if starts_with:
        cat_list = Category.objects.filter(name__istartswith=starts_with)

    if max_results > 0:
        if len(cat_list) > max_results:
            cat_list = cat_list[:max_results]

    return cat_list


def suggest_category(request):

    cats = []
    starts_with = request.GET['suggestion'] or ''
    cats = get_category_list(8, starts_with)
    context = {'cats': cats}

    return render(request, 'rango/cats.html', context)


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


def register(request):

    registered = False
    user_form = UserForm(request.POST or None)
    profile_form = UserProfileForm(request.POST or None)

    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save()
        user.set_password(user.password)
        user.save()
        profile = profile_form.save(commit=False)
        profile.user = user

        if 'picture' in request.FILES:
            profile.picture = request.FILES['picture']

        profile.save()
        registered = True

    return render(request,
            'rango/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

