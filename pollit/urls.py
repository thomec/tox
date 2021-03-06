"""URL Routing for pollit"""

from django.conf.urls import patterns, url

from pollit import views
from pollit.models import Poll

COMMENT_INFO_DICT = {
    'queryset': Poll.objects.filter(status__lt=3, comment_status__gt=1),
    'template_object_name': 'poll',
    'date_field': 'pub_date',
    'template_name': 'pollit/comments.html'
}

YMDS_REGEX = r'(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/(?P<slug>[\w\-]+)/'

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^(?P<poll>\d+)/$', views.index, name='detail'),
    #url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<slug>[\w\-]+)/$', 'pollit.views.detail_old', name='pollit_detail_old'),
    #url('^%s$' % YMDS_REGEX, 'pollit.views.detail', name='pollit_detail'),
    #url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<slug>[\w\-]+)/results/$', 'pollit.views.results_old', name='pollit_results_old'),
    #url(r'^{0}results/$'.format(YMDS_REGEX), 'pollit.views.results', name='pollit_results'),
    url('^%scomments/$' % YMDS_REGEX,
        'django.views.generic.date_based.object_detail',
        kwargs=COMMENT_INFO_DICT,
        name='pollit_comments')
)
