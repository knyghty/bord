from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^register/$', views.RegistrationView.as_view(), name='register'),
]
