from django.conf.urls import url, include
from django.views.generic import RedirectView
from .views import get_testimonials, testimonial_detail, create_or_edit_testimonial

urlpatterns = [
    url(r'^$', get_testimonials, name='get_testimonials'),
    url(r'^(?P<pk>\d+)/$', testimonial_detail, name='testimonial_detail'),
    url(r'^new/$', create_or_edit_testimonial, name='new_testimonial'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_testimonial, name='edit_testimonial'),
    #url(r'^.*$', RedirectView.as_view(url='/', permanent=False), name='index')
]