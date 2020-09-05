from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'Jazariyyah'

urlpatterns = [
    url(r'^$', views.JazariyyahList.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$',
        views.JazariyyahDetail.as_view(), name='detail'),

]
