"""AKEP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from items.views import IndexView,Update,Person_detail,Rank,EP
import os

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^custom/(?P<path>.*)', serve,{"document_root":os.path.join(settings.BASE_DIR,'custom')}),
    url(r'^$', IndexView),
    url(r'^person/(?P<name>.*)$', Person_detail),
    url(r'^rank/$', Rank),
    url(r'^ep/$', EP),
    url(r'^update/(?P<id>\d+)/$', Update),
]
