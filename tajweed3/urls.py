from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'tajweed3'

urlpatterns = [
    url(r'^$', views.Tajweed3List.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$', views.Tajweed3Detail.as_view(), name='detail'),

]
