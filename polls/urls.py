# polls/urls.py


from django.conf.urls import patterns, url
from django.contrib import admin
from polls import views


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^poll/(?P<poll_id>\d+)/$', views.detail, name='detail'),
        url(r'^question/(?P<question_id>\d+)/$', views.question, name='question'),
        url(r'^question/(?P<question_id>\d+)/vote/', views.vote, name='vote'),
        url(r'^question/(?P<question_id>\d+)/results/', views.results, name='results'),
        url(r'^add_poll/$', views.add_poll, name='add_poll'),
        url(r'^poll/(?P<poll_id>\d+)/add_question/$', views.add_question, name='add_question'),
        url(r'^question/(?P<question_id>\d+)/add_answer/$', views.add_answer, name='add_answer'),
        url(r'^new_poll/$', views.new_poll, name='new_poll'),
        url(r'^poll/(?P<poll_id>\d+)/edit_poll/$', views.edit_poll, name='edit_poll'),
        url(r'^question/(?P<question_id>\d+)/edit_question/$', views.edit_question, name='edit_question')
)
