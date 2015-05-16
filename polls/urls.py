# polls/urls.py


from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^(?P<poll>\d+)/$', views.poll, name='poll'),
        url(r'^question/(?P<question>\d+)/$', views.question, name='question'),
        url(r'^(?P<poll>\d+)/results/$', views.results, name='results'),
        url(r'^(?P<question>\d+)/vote/$', views.vote, name='vote'),
        )
