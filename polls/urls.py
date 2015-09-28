# polls/urls.py


from django.conf.urls import patterns, url

from polls import views



urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^poll/(?P<poll>\d+)/$', views.poll, name='poll'),

        url(r'^poll/(?P<poll>\d+)/edit', views.edit, name='edit'),
        
        url(r'^polls/$', views.polls, name='polls'),
        #url(r'^questions/$', views.questions, name='questions'),
                #url(r'^question/(?P<question>\d+)/$', views.question, name='question'),
        url(r'^(?P<poll>\d+)/results/$', views.results, name='results'),
)
