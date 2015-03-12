import urllib
from django.conf import settings
from django.core.urlresolvers import reverse


class GithubManager(object):
    def get_github_url(self):
        domain = settings.BASE_DOMAIN
        base_url = 'https://github.com/login/oauth/authorize'
        redirect = '{0}{1}'.format(domain, reverse('github:callback'))

        scopes = (
            'user:email',
            'read:org',
            'repo_deployment',
            'repo:status',
            'write:repo_hook'
        )

        params = {
            'client_id': settings.GITHUB_CLIENT_ID,
            'redirect_uri': redirect,
            'scope': ','.join(scopes)
        }
        parsed_params = urllib.urlencode(params)
        url = '{0}?{1}'.format(base_url, parsed_params)
        return url
