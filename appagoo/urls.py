# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from rest_framework import routers

from users.views import UserViewSet
from profiles.views import ThreatViewSet, ProfileViewSet
from apps.views import ApplicationViewSet, CategoryViewSet, DownloadsViewSet

admin.autodiscover()


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'applications', ApplicationViewSet)
router.register(r'downloads', DownloadsViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'profiles', ProfileViewSet, base_name='profiles')
router.register(r'threats', ThreatViewSet)
router.register(r'users', UserViewSet, base_name='users')


urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    #url(r'^api/login/', LoginView.as_view(), name='login'),
    #url(r'^api/login-token/', LoginTokenView.as_view(), name='login-token'),
    #url(r'^api/logout/', LogoutView.as_view(), name='logout'),
    url(r'^api-token/', include('allauth.urls')),
    patterns('django.contrib.staticfiles.views',
        url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'index.html'}),
        url(r'^(?P<path>(?:js|css|img)/.*)$', 'serve'),
    ),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),

    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/logged/',
        TemplateView.as_view(template_name='account/logged.html'),
        name="logged"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)