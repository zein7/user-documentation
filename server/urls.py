from django.conf.urls import include, url

urlpatterns = [
    url(r'^fafl', include('fafl.urls')),
    url(r'^', include('aristotle_mdr.urls')),
    url(r'^browse/', include('aristotle_mdr.contrib.browse.urls')),
    url(r'^help/', include('aristotle_mdr.contrib.help.urls', app_name="aristotle_help", namespace="aristotle_help")),
    url(r'^publish/', include('aristotle_mdr.contrib.self_publish.urls', app_name="aristotle_self_publish", namespace="aristotle_self_publish")),
    url(r'^', include('aristotle_mdr.contrib.links.urls', app_name="aristotle_mdr_links", namespace="aristotle_links")),
    url(r'^', include('aristotle_mdr.contrib.slots.urls', app_name="aristotle_slots", namespace="aristotle_slots")),
    url(r'^', include('aristotle_mdr.contrib.identifiers.urls', app_name="aristotle_mdr_identifiers", namespace="aristotle_identifiers")),
]
