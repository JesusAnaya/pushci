from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^github/', include('github.urls', namespace='github')),
    url(r'^admin/', include(admin.site.urls)),
)
