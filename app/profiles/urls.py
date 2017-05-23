from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from constance import config
from . import views

admin.site.site_header = config.SITE_NAME + ' Admin'
admin.site.index_title =  config.SITE_NAME + ' Admin'
admin.site.site_title =  config.SITE_NAME

urlpatterns = [
    url(r'^me$', views.ShowProfile.as_view(), name='show_self'),
    url(r'^me/edit$', views.EditProfile.as_view(), name='edit_self'),
    url(r'^(?P<slug>[\w\-]+)$', login_required(views.ShowProfile.as_view()),
        name='show'),
]
