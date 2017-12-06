from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^/$', views.home, name="home"),
    url(r'^/edit$', views.edit, name="editor"),
    url(r'^/dumper$', views.dumper, name="dumper"),
    url(r'^/loader', views.loader, name="loader"),
    url(r'^/reset', views.resetter, name="resetter"),
    url(r'^/raw/(.*)', views.raw),
    url(r'^/help', views.help, name="help"),
]
