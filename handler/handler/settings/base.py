"""
Django settings for handler project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from datetime import timedelta

from django.utils.translation import gettext_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '_s6z7+petc18ijfuw$#+o0ach%f1&gv-(w2(3ek51+r@x9%-)z')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True').lower() in ('true', '1', 'yes')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '{levelname:5} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'default'},
        'mail_admins': {'level': 'ERROR', 'class': 'django.utils.log.AdminEmailHandler'}
    },
    'loggers': {
        'django': {'level': 'INFO', 'handlers': ['console']},
        'django.request': {'level': 'ERROR', 'handlers': ['console', 'mail_admins'], 'propagate': False},
        'celery': {'level': 'INFO', 'handlers': ['console']},
        'handler': {'level': 'DEBUG', 'handlers': ['console']},
        'channels': {'level': 'DEBUG', 'handlers': ['console']},
        'daphne': {'level': 'DEBUG', 'handlers': ['console']},
        'twisted': {'level': 'DEBUG', 'handlers': ['console']},
    }
}

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.humanize',
    'django.contrib.postgres',

    'channels',
    'django_extensions',
    'rest_framework',
    'rest_framework_gis',
    'django_filters',
    'crispy_forms',
    'django_celery_beat',

    'handler',
]


MIDDLEWARE = [
    'handler.middleware.CommonMiddleware',
    'handler.middleware.DoNotTrackMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'handler.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
        ],
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
]

WSGI_APPLICATION = 'handler.wsgi.application'
ASGI_APPLICATION = 'handler.routing.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'handler',
        'USER': 'rds',
        'PASSWORD': 'sqlsql',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },

    'sensor': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'sensor',
        'USER': 'rds',
        'PASSWORD': 'sqlsql',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/2',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'SERIALIZER': 'django_redis.serializers.json.JSONSerializer',
            # 'SERIALIZER': 'django_redis.serializers.pickle.PickleSerializer',
            # 'COMPRESSOR': 'django_redis.compressors.zlib.ZlibCompressor',
            # 'PICKLE_VERSION': -1,
            'IGNORE_EXCEPTIONS': True,
        }
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            # "hosts": [('127.0.0.1', 6379)],
            "hosts": [{"address": ('127.0.0.1', 6379), "db": 2}],
            "prefix": "micro",
        },
    },
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    # {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    # {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    # {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', gettext_lazy('English')),
    ('ru', gettext_lazy('Russian')),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/api/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# REST_FRAMEWORK

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,

    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),

    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.ScopedRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '50/m',
        'user': '200/m',
        'login': '3/m',
    },
    # 'NUM_PROXIES': 1,
}

# CELERY
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/2'
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_WORKER_MAX_TASKS_PER_CHILD = 10
CELERY_WORKER_MAX_MEMORY_PER_CHILD = 512 * 1024
CELERY_RESULT_EXPIRES = timedelta(hours=1)
CELERY_BEAT_SCHEDULE = {
    # Executes at sunset in Melbourne
    'import_sensor1': {
        'task': 'import_sensor1',
        'schedule': 10,
    },
    'import_sensor2': {
        'task': 'import_sensor2',
        'schedule': 60,
    },
}
