__author__ = 'Nigga'
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'poll/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'poll/logout.html'}),
    url(r'^form/$', views.reg),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^password-reset/$', password_reset, name='password_reset'),
    url(r'^password-reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', password_reset_complete, name='password_reset_complete'),

]