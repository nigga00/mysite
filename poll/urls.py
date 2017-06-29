__author__ = 'Nigga'
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'poll/login.html'}),
    url(r'^form/$', views.reg),

]