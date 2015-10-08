# rango/urls.py


from django.conf.urls import patterns, url

from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^category/(?P<slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^category/(?P<slug>[\w\-]+)/add_page/$',
            views.add_page,
            name='add_page'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^add_profile/$', views.add_profile, name='add_profile'),
        url(r'^profile/$', views.profile, name='profile'),
        url(r'^search/$', views.search, name='search'),
        url(r'^goto/(?P<page>\d+)/$', views.track, name='goto'),
        url(r'^like_category/$', views.like_category, name='like_category'),
)


