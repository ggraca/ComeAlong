from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^new/$', views.new),
    url(r'^(?P<id>\d+)/$', views.page),
)