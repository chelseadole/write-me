"""imagersite URL Configuration."""
from django.conf.urls import url
from imager_profile.views import profile_view, profile_request


urlpatterns = [
    # url(r'^$', views.profile_view, name="profile"),
    url(r'(?P<username>\w+)$', profile_request, name="profile"),
    url(r'^$', profile_view, name="profile_authenticated")
]
