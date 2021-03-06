"""Settings for BORD."""

import os

import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Useful constants.

_TRUTHY_STRINGS = ('true', 'yes', 'on')


# Useful functions.

def _getenv_bool(key):
    value = os.environ.get(key, 'false')
    return value.lower() in _TRUTHY_STRINGS


# Security stuff.

ALLOWED_HOSTS = ['bord.cricket', 'www.bord.cricket', 'bord-red-dragon.herokuapp.com']

DEBUG = _getenv_bool('DEBUG')

SECRET_KEY = os.environ['SECRET_KEY']


# Application definition

INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party
    'anymail',
    # Local
    'accounts',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bord.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': True,
        },
    },
]

WSGI_APPLICATION = 'bord.wsgi.application'


# Database.

DATABASES = {
    'default': dj_database_url.config(),
}


# Authentication.

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'accounts.User'

LOGIN_REDIRECT_URL = '/'


# Internationalization.

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files.

STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

STATIC_URL = '/static/'


# Email

ADMINS = [('Tom Carrick', 'knyght+bord@knyg.ht')]

ANYMAIL = {
    'MAILGUN_API_KEY': 'key-49b5617b8deeb55831bb49c0b72623c4',
}

DEFAULT_FROM_EMAIL = 'noreply@bord.cricket'

EMAIL_BACKEND = 'anymail.backends.mailgun.MailgunBackend'
