from django.conf.urls import url
from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

app_name = 'tutapp'

urlpatterns = [
    url(r'^$', views.AudioClipList.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$', views.AudioClipDetail.as_view(), name='detail'),
    url(r'login/$', auth_views.LoginView.as_view(template_name='signin.html'), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'signup/$', views.SignUp.as_view(), name='signup')
]
