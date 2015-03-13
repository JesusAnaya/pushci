import requests


class GithubApi3Exception(Exception):
    pass


class GithubApi3(object):
    base_url = 'https://api.github.com'

    def __init__(self, access_token=None):
        self.access_token = access_token

    def headers(self):
        headers_values = {
            'Accept': 'application/vnd.github.v3+json',
            'Accept': 'application/json'
        }

        if self.access_token:
            token = 'token {0}'.format(self.access_token)
            headers_values['Authorization'] = token
        return headers_values

    def get_access_token(self, params):
        url = 'https://github.com/login/oauth/access_token'
        response = self.post(url, params)

        if response.status_code != 200:
            raise GithubApi3Exception(
                "Error getting access token: code: {0}, {1}".format(
                    response.status_code, response.content))
        return response.json()

    def get_user_info(self, access_token):
        url = '/user?access_token={0}'.format(access_token)
        response = self.get(url)

        if response.status_code != 200:
            raise GithubApi3Exception(
                "Error getting user info: code: {0}, {1}".format(
                    response.status_code, response.content))
        return response.json()

    def get_user_repos(self):
        url = '/user/repos'
        response = self.get(url)

        if response.status_code != 200:
            raise GithubApi3Exception(
                "Error getting user repos: code: {0}, {1}".format(
                    response.status_code, response.content))
        return response.json()

    def get(self, api_url):
        url = '{0}{1}'.format(self.base_url, api_url)
        response = requests.get(
            url, headers=self.headers(), verify=False, allow_redirects=False)
        return response

    def post(self, api_url, params={}):
        url = '{0}{1}'.format(self.base_url, api_url)
        response = requests.post(
            url, headers=self.headers(), data=params,
            verify=False, allow_redirects=False)
        return response
