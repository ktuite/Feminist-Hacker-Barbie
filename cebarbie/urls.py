from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cebarbie.views.index', name='index'),
    url(r'^browse$', 'cebarbie.views.browse', name='browse'),
    url(r'^evil_browse$', 'cebarbie.views.evil_browse', name='evil_browse'),
    url(r'^new$', 'cebarbie.views.new_panel', name='new_panel'),
    url(r'^view/(?P<id>[0-9]+)$', 'cebarbie.views.view_panel', name='view_panel'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^save_page$', 'cebarbie.views.save_page', name='save_page'),
    url(r'^endorse$', 'cebarbie.views.endorse', name='endorse'),
    url(r'^delete$', 'cebarbie.views.delete', name='delete'),
    url(r'^flag$', 'cebarbie.views.flag', name='flag'),

    url(r'^admin/', include(admin.site.urls)),
)
