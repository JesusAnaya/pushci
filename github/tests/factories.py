import factory
from django.conf import settings


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL
    username = 'john'
    email = 'yo@example.com'


class GithubFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'github.Github'

    user = factory.SubFactory(UserFactory)
    name = 'UserFake'
    user_name = 'User Fake Second'
    account_id = 123456
    email = 'yo@example.com'
    access_token = 'aa123456677'
