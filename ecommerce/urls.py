from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts, urls_reset
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT
from home import views
from home.views import index
from home.views import about
from blog import urls as urls_blog
from posts import urls as urls_posts
from posts.views import get_posts
from posts.views import post_detail
from testimonials import urls as urls_testimonials
from testimonials.views import get_testimonials
from testimonials.views import testimonial_detail
from testimonials.views import create_or_edit_testimonial
from posts.views import create_or_edit_post
from avatar import urls as avatar_urls
from accounts.views import editprofile
from checkout import urls as urls_checkout
from django.views.generic import RedirectView
from home import urls as urls_home
from djreservation import urls as djreservation_urls



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^faqs/', include(urls_posts)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^home/', include('home.urls')),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^accounts/password-reset/', include(urls_reset)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^testimonials/', include(urls_testimonials)),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
] + djreservation_urls.urlpatterns
