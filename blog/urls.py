from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/unpublish/$', views.post_unpublish, name='post_unpublish'),
    url(r'^post/new/$', views.post_new, name='post_new'),

)
