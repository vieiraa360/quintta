from django.conf.urls import url
from ecommerce import settings
from avatar import views
from django.views.static import serve
from ecommerce.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^add/$', views.add, name='avatar_add'),
    url(r'^change/$', views.change, name='avatar_change'),
    url(r'^delete/$', views.delete, name='avatar_delete'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^render_primary/(?P<user>[\w\d\@\.\-_]+)/(?P<size>[\d]+)/$',
        views.render_primary,
        name='avatar_render_primary'),
]
