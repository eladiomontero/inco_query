from django.conf.urls import patterns, include, url
from django.contrib import admin
import incoquery.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', incoquery.views.ListQueryView.as_view(),
        name = 'query-list',),

    url(r'^new$', incoquery.views.CreateQueryView.as_view(),
        name='query-new',),

    url(r'^edit/(?P<pk>\d+)/$', incoquery.views.UpdateQueryView.as_view(),
        name='query-edit',),
]

urlpatterns += staticfiles_urlpatterns()