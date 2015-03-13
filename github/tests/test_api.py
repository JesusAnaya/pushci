from django.test import TestCase
from github.api import GithubApi3, GithubApi3Exception
from mock import patch, MagicMock
import json


class GithubApi3TestCase(TestCase):
    def setUp(self):
        self.patcher_requests = patch('github.api.requests')
        self.requests = self.patcher_requests.start()

        self.api = GithubApi3()

    def tearDown(self):
        self.patcher_requests.stop()

    def test_get_access_token_using_code_param(self):
        expected_response = MagicMock(name='response')
        expected_response.status_code = 200
        expected_response.content = '{"access_token":"1234567890",' \
            '"scope":"repo,gist","token_type":"bearer"}'
        content_parsed = json.loads(expected_response.content)
        expected_response.json.return_value = content_parsed
        self.requests.post.return_value = expected_response

        params = {
            'client_id': '123456',
            'client_secret': 'aabb123456',
            'code': 'abcd123'
        }
        response = self.api.get_access_token(params)
        self.assertDictEqual(response, content_parsed)

    def test_error_getting_access_token(self):
        expected_response = MagicMock(name='response')
        expected_response.status_code = 400
        expected_response.content = '{"error":"bad request"}'
        self.requests.post.return_value = expected_response
        error_message = ''

        try:
            self.api.get_access_token({})
        except GithubApi3Exception as error:
            error_message = str(error)

        error_msg = 'Error getting access token: code: 400, ' \
            '{"error":"bad request"}'
        self.assertEqual(error_message, error_msg)
