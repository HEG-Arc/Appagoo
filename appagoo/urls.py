# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from rest_framework import routers

from users.views import UserViewSet, LoginView
from profiles.views import ProfileViewSet, ThreatViewSet
from apps.views import ApplicationViewSet, CategoryViewSet, DownloadsViewSet

admin.autodiscover()


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'applications', ApplicationViewSet)
router.register(r'downloads', DownloadsViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'threats', ThreatViewSet)
router.register(r'users', UserViewSet)


urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api/login/', LoginView.as_view(), name='login'),
    url(r'^$',  # noqa
        TemplateView.as_view(template_name='index.html'),
        name="home"),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)