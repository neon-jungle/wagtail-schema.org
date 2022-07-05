import os

from wagtail import VERSION as WAGTAIL_VERSION

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(TESTS_DIR)


INSTALLED_APPS = [
    'tests.app',

    'wagtailschemaorg',

    'wagtail.users',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail' if WAGTAIL_VERSION >= (3, 0) else 'wagtail.core',
    'wagtail.contrib.settings',

    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'wagtail.middleware.SiteMiddleware' if WAGTAIL_VERSION >= (3, 0) else 'wagtail.core.middleware.SiteMiddleware',
]

ROOT_URLCONF = 'tests.app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'OPTIONS': {
            'extensions': [
                'wagtailschemaorg.jinja2tags.WagtailSchemaOrgExtension',
            ],
        },
    },
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(TESTS_DIR, 'db.sqlite3'),
    }
}


LANGUAGE_CODE = 'en-au'
TIME_ZONE = 'Australia/Hobart'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_ROOT = os.path.join(TESTS_DIR, 'assets', 'static')
MEDIA_ROOT = os.path.join(TESTS_DIR, 'assets', 'media')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

WAGTAIL_SITE_NAME = "Wagtail Schema.org test suite"

if WAGTAIL_VERSION >= (3, 0):
    WAGTAILADMIN_BASE_URL = 'http://example.com'
else:
    BASE_URL = 'http://example.com'

DEBUG = True

SECRET_KEY = 'not a secret'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
