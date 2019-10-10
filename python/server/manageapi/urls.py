from django.conf.urls import include, url
from .views import ManageDotApi

urlpatterns = [
    url(r'^(?P<command>.+)/?$', ManageDotApi.as_view(), name='manage.api'),
]
