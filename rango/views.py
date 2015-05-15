# rango/views.py


from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm


def index(request):
    
    context = {}
    context['categories'] = Category.objects.order_by('-likes')
    context['pages'] = Page.objects.order_by('-views')

    return render(request, 'rango/index.html', context)


def about(request):
    return render(request, 'rango/about.html')


def category(request, slug):
    
    category = get_object_or_404(Category, slug=slug)    
    pages = Page.objects.filter(category=category)
    context = {'category': category, 'pages': pages,}
    
    return render(request, 'rango/category.html', context)


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





class IndexView(TemplateView):
    template_name = 'rango/index.html'
    queryset = Category.objects.order_by('-likes')[:5]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['message'] = "Rango Index"
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        categories = Category.objects.order_by('-likes')[:5]
        return self.render_to_response(context)
    
class AboutView(TemplateView):
    template_name = 'rango/about.html'
    

