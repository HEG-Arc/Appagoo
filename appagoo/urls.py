# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from rest_framework import routers

from apps.views import ApplicationViewSet, CategoryViewSet, DownloadsViewSet

admin.autodiscover()


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'applications', ApplicationViewSet)
router.register(r'downloads', DownloadsViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^$',  # noqa
        TemplateView.as_view(template_name='index.html'),
        name="home"),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable avatars
    url(r'^avatar/', include('avatar.urls')),

    # Your stuff: custom urls go here
    url(r'^apps/', include('apps.urls')),

     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)