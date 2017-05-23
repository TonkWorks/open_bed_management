
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import profiles.urls
import accounts.urls

import rest_framework
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views as auth_views
from rest_framework import generics

from website.views import HomePage
from website.views import DashboardPage
from beds.views import BedViewSet
from beds.views import LogViewSet
from beds.views import StatusViewSet
from beds.views import TagViewSet

from beds.views import SettingsViewSet

# # TODO Move to API Customizations
class Router(routers.DefaultRouter):
    def get_api_root_view(self, api_urls=None):
        root_view = super(Router, self).get_api_root_view(api_urls=api_urls)
        root_view.cls.__name__ = "API"
        root_view.cls.__doc__ = "API"
        return root_view

router = Router()
router.register(r'beds', BedViewSet, base_name='beds')
router.register(r'tags', TagViewSet, base_name='tags')
router.register(r'statuses', StatusViewSet, base_name='statuses')
router.register(r'logs', LogViewSet, base_name='logs')
router.register(r'settings', SettingsViewSet, base_name='settings')

urlpatterns = [
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^dashboard/$', DashboardPage.as_view(), name='dashboard'),

    url(r'^api-token-auth/$', auth_views.obtain_auth_token),

    url(r'^api/', include(router.urls), name='api'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

    # User-uploaded files like profile pics need to be served in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
