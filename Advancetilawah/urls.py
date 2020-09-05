from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'Advancetilawah'

urlpatterns = [
    url(r'^$', views.AdvancetilawahList.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$',
        views.AdvancetilawahDetail.as_view(), name='detail'),

]
