from django.conf.urls import patterns, url
from django.views.generic import TemplateView

import views

urlpatterns = patterns('',
    url(r'^$', views.index,  name='index'),
    url(r'^search/$', views.search),
)