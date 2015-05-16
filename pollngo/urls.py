from django.conf.urls import *
#from django.views.generic.simple import direct_to_template

from pollngo import views



urlpatterns = patterns('', #'pollngo.views',
    url(r'^$', views.index, name='index'),
    url(r'^poll/(?P<slug>[^\.^/]+)/$', views.question, name='question'),
    url(r'^create/$', views.create, name='create'),
    url(r'^help/$', views.help, name='help'),
    url(r'^results/(?P<slug>[^\.^/]+)/$', views.results, name='results'),
    )
