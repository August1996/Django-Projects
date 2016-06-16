"""mysite URL Configuration

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
from django.views.static import serve
from django.contrib import admin
from django.conf import settings
from blog.views import index,article,articles,tag,search,category,about
from blog.upload import upload_image
import os
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index,name='index'),
    url(r'^index/$', index,name='index'),
    url(r'^article/(?P<id>\d+)/$', article,name='article'),
    url(r'^articles/(?P<page>\d+)/$', articles,name='articles'),
    url(r'^tag/(?P<id>\d+)/(?P<page>\d+)/$', tag,name='tag'),
    url(r'^category/(?P<id>\d+)/(?P<page>\d+)/$', category,name='category'),
    url(r'^search/(?P<keyword>.*)/(?P<page>\d+)/$', search,name='search'),
    url(r'^about/$', about,name='about'),
    url(r'^static/(?P<path>.*)', serve,{'document_root':os.path.join(settings.BASE_DIR,'static')}),
    url(r'^uploads/(?P<path>.*)/$', serve,{'document_root':os.path.join(settings.BASE_DIR,'uploads')}),
    url(r'^admin/upload', upload_image, name='upload_image'),
]
