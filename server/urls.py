from django.conf.urls import include, url

urlpatterns = [
    url(r'^fafl', include('fafl.urls')),
    url(r'^', include('aristotle_mdr.urls')),
]
