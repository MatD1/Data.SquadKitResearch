"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from pathlib import Path
# reading .env file
#environ.Env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #env('DEBUG')

ALLOWED_HOSTS = ['localhost:8000', 'http://localhost:8000', 'http://localhost:3000', 'localhost:3000','railway.squadkitresearch.net', 'web-production-a41d.up.railway.app', 'https://squadkitresearch.net', 'squadkitresearch.net']


# Application definition

INSTALLED_APPS = [
    'django_admin_env_notice',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapi.apps.MyapiConfig',
    "Weapons",
    'rest_framework',
    "rest_framework_api_key",
    "django_filters",
    'corsheaders',
    "sslserver",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django_admin_env_notice.context_processors.from_settings",
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["PGDATABASE"],
        'USER': os.environ["PGUSER"],
        'PASSWORD': os.environ["PGPASSWORD"],
        'HOST': os.environ["PGHOST"],
        'PORT': os.environ["PGPORT"],
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Sydney'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        #'rest_framework.permissions.DjangoModelPermissions',
        #"rest_framework_api_key.permissions.HasAPIKey",


    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '0/day',
        'user': '1000/hour'
    }

}

CORS_ALLOWED_ORIGINS = [
    'https://squadkitresearch.net',
    'http://localhost:3000',
]

sentry_sdk.init(
    dsn="https://6bd32a164eea401b9db0603478759a2f@o1247526.ingest.sentry.io/6724676",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

# Caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': os.environ['REDIS'],
    }
}

# Configure Django App for Heroku.
# import django_heroku
# django_heroku.settings(locals())
# Security Settings
SECURE_HSTS_SECONDS = os.environ['SECURE_HSTS_SECONDS']
SECURE_SSL_REDIRECT = os.environ['SECURE_SSL_REDIRECT']
SESSION_COOKIE_SECURE = os.environ['SESSION_COOKIE_SECURE']
CSRF_COOKIE_SECURE = os.environ['CSRF_COOKIE_SECURE']
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ['SECURE_HSTS_INCLUDE_SUBDOMAINS']
SECURE_HSTS_PRELOAD = os.environ['SECURE_HSTS_PRELOAD']
# CORS
CORS_ALLOW_CREDENTIALS = False

#Thousands Seperator
USE_THOUSAND_SEPARATOR = True

# Django admin enviroment Notice
ENVIRONMENT_NAME = "Production server"
ENVIRONMENT_COLOR = "#13E55F"
ENVIRONMENT_NAME = "Development server"
ENVIRONMENT_COLOR = "#F40505"
ENVIRONMENT_FLOAT = True
