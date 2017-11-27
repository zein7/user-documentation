from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^/$', views.home),
    url(r'^/edit$', views.edit, name="editor"),
    url(r'^/dumper$', views.dumper, name="dumper"),
    url(r'^/raw/(.*)', views.raw),
]
