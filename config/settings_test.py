from config.settings import *

DEBUG = True
TEMPLATE_DEBUG = True

GITHUB_CLIENT_ID = '1234567890'
BASE_DOMAIN = 'http://example.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
    }
}
