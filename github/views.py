from django.views.generic import RedirectView
from github.managers import GithubManager


class GihubMixin(object):
    def manager(self):
        return GithubManager()


class GithubLoginPage(GihubMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        return self.manager().get_github_url()
