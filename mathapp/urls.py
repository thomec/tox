# mathapp/urls.py


from django.conf.urls import patterns, url

from mathapp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        #url(r'^index/$', views.index, name='index'),
        url(r'^submit_survey/$', views.about, name='about'),
)
