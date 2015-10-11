from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import news.urls

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'dragwebnews.views.homepage', name='home'),
    url(r'^headline/', include('news.urls')),
)
