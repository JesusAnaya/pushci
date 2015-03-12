from django.conf.urls import patterns, url
from github.views import GithubLoginPage
from django.views.generic import View


urlpatterns = patterns(
    '',
    url(r'^authorize/$', GithubLoginPage.as_view(), name='authorize'),
    url(r'^callback/$', View.as_view(), name='callback'),
)
