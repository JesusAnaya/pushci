from django.test import TestCase
from django.core.urlresolvers import reverse


class GithubViewsTest(TestCase):
    def setUp(self):
        pass

    # GithubLoginPage()
    def test_redirection_to_github(self):
        url = reverse('github:authorize')
        expected_url = 'https://github.com/login/oauth/authorize?' \
            'scope=user%3Aemail%2Cread%3Aorg%2Crepo_deployment' \
            '%2Crepo%3Astatus%2Cwrite%3Arepo_hook&' \
            'redirect_uri=http%3A%2F%2Fexample.com' \
            '%2Fgithub%2Fcallback%2F&client_id=1234567890'

        response = self.client.get(url)
        self.assertEquals(response.url, expected_url)
        self.assertEquals(response.status_code, 302)
