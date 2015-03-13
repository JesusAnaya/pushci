from django.test import TestCase
from github.tests.factories import GithubFactory


class GithubModelTestCase(TestCase):
    def setUp(self):
        self.github = GithubFactory.create()

    def test_validate_correct_stringify_of_model(self):
        self.assertEquals(unicode(self.github), 'john - User Fake Second')
