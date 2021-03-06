# tox/urls.py

"""
tox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""


from django.conf.urls import include, url, patterns
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

# wenn DEBUG = False
from django.conf import settings
from django.conf.urls.static import static


# overwrite success_url in redux when registration complete
class MyRegistrationView(RegistrationView):
    # modify urlpatterns so that accounts/register
    # points to MyRegistrationView.as_view()
    def get_success_url(self, request, user):
        return '/rango/'



urlpatterns = [
        #url(r'^$', include('rango.urls', namespace='rango')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^rango/', include('rango.urls', namespace='rango')),
        url(r'^polls/', include('polls.urls', namespace='polls')),
        url(r'^pollit/', include('pollit.urls', namespace='pollit')),
        url(r'^pollngo/', include('pollngo.urls', namespace='pollngo')),
        url(r'^accounts/', include('registration.backends.simple.urls')),
        #url(r'^accounts/', include('registration.backends.default.urls')),
        url(r'^mathapp/', include('mathapp.urls', namespace='ma'))
        ]

if settings.DEBUG:
    urlpatterns += patterns(
            'django.views.static',
            (
                    r'^media/(?P<path>.*)',
                    'serve',
                    {'document_root': settings.MEDIA_ROOT}
                    ),
            )
else:
    urlpatterns += static(
            settings.STATIC_URL,
            settings.MEDIA_URL,
            document_root=settings.STATIC_ROOT,
            )
# endewenn

