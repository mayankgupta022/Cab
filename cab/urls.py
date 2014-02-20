from django.conf.urls import patterns, include, url
from cab import settings
from coms.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', writeup, {}),
    # Examples:
    # url(r'^$', 'cab.views.home', name='home'),
    # url(r'^cab/', include('cab.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',  
     {'document_root': settings.MEDIA_ROOT}),
    (r'^snippets/', include('social.urls.snippets')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<name>[-\w]+)/$', writeup, {}),
)
