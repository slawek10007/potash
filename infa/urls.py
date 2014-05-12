from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import home.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'infa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home.views.Widok.as_view(), name='widok')
)
