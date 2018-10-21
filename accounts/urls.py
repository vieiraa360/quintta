from django.conf.urls import url, include
from . import urls_reset
from accounts import views
from .views import index, register, profile, logout, login, editprofile

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^profile/edit/$', views.editprofile, name='editprofile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
]