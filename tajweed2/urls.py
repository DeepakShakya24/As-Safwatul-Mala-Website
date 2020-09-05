from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'tajweed2'

urlpatterns = [
    url(r'^$', views.Tajweed2List.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$', views.Tajweed2Detail.as_view(), name='detail'),

]
