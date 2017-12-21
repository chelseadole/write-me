"""imagersite URL Configuration."""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from imager_images.views import image_view

from imager_profile.views import library_view

from imagersite import settings
from imagersite import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^profile/', include('imager_profile.urls')),
    url(r'^images/library/$', library_view, name='library'),
    url(r'^images/photos/(?P<pk>\d+)/$', image_view, name='single_image'),
    url(r'^images/albums/(?P<pk>\d+)/$', image_view, name='single_image'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
