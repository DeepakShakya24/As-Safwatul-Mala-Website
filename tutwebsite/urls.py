from django.contrib import admin
from django.conf.urls import url, include
#from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from tutapp import views
urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^homepage/', views.homepage, name='homepage'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='signin.html'), name='login'),
    url(r"signup/", views.SignUp.as_view(), name="signup"),
    url(r'^$', views.AudioClipList.as_view(), name='list'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^index/', views.index, name='index'),
    url(r'^about/', views.About, name='about'),
    url(r'^aboutus/', views.AboutUs, name='aboutus'),
    url(r'^whatistajweed/', views.Whatistajweed, name='whatistajweed'),
    url(r'^importanceoftajweed/', views.Importanceoftajweed,
        name='importanceoftajweed'),
    url(r'^reset_password/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'), name='reset_password'),
    url(r'^reset_paasword_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_sent.html'), name='password_reset_done'),
    url(r'^reset_confirmation/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirmation.html'), name='password_reset_confirm'),
    url(r'^reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_complete'),
    url(r'^admin/', admin.site.urls),
    url(r'tutapp/', include('tutapp.urls', namespace='tutapp')),
    url(r'tajweed2/', include('tajweed2.urls')),
    url(r'tajweed3/', include('tajweed3.urls')),
    url(r'advancetilawah/', include('Advancetilawah.urls')),
    url(r'jazariyyah/', include('Jazariyyah.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
