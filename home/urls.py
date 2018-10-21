from django.conf.urls import url
from django.views.generic import RedirectView
from home import views


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
]