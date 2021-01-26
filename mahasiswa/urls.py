from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/$', views.api_create_and_view),
    url(r'^api/(?P<pk>[0-9]+)$', views.api_viewbyid_update_delete),
]
