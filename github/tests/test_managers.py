from django.test import TestCase
from mock import MagicMock
from github.managers import GithubManager


class GithubTestCase(TestCase):
    def setUp(self):
        self.api_class = self.api = MagicMock(name='api')
        self.manager = GithubManager()

    # get_github_url()
    def test_get_custom_url_for_github_auth(self):
        response = self.manager.get_github_url()
        expected_url = 'https://github.com/login/oauth/authorize?' \
            'scope=user%3Aemail%2Cread%3Aorg%2Crepo_deployment' \
            '%2Crepo%3Astatus%2Cwrite%3Arepo_hook&' \
            'redirect_uri=http%3A%2F%2Fexample.com' \
            '%2Fgithub%2Fcallback%2F&client_id=1234567890'
        self.assertEquals(response, expected_url)
