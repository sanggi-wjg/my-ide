"""
Django settings for my_ide project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import json
import logging
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

def read_json(path):
    with open(path) as json_file:
        json_data = json.load(json_file)
        return json_data


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_json(os.path.join(BASE_DIR, 'my_ide', 'secret_key.json'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG_TOOLBAR = True

ALLOWED_HOSTS = [
    '218.146.5.52'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'home',
    'common',
    'dockers',
    'ide',
    'snippets',

    "debug_toolbar",
]

# DEBUG TOOLBAR
INTERNAL_IPS = [
    '127.0.0.1',
    '218.146.5.41'
]

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'my_ide.urls'

TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates',
        'DIRS'    : [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS' : {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins'          : ['dockers.templatetags.help_tags']
        },
    },
]

WSGI_APPLICATION = 'my_ide.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME'  : BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

root = logging.getLogger()
root.setLevel('DEBUG')

LOGGING = {
    'version'                 : 1,
    'disable_existing_loggers': False,
    'formatters'              : {
        'basic': {
            'format': '[%(levelname)s] [%(asctime)s] (%(name)s) %(message)s'
        }
    },
    'handlers'                : {
        'console': {
            'level'    : os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
            'class'    : 'logging.StreamHandler',
            'formatter': 'basic',
        },
    },
    'root'                    : {
        'level'   : os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        'handlers': ['console'],
    },
    'loggers'                 : {
        'django'            : {
            'level'    : os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'handlers' : ['console'],
            'propagate': False,
        },
        'django.db.backends': {
            'level'    : os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'handlers' : ['console'],
            'propagate': False,
        },
    },
}

########################################
# Below Custom Setting values
########################################

# about dockerfile
DOCKERFILES_ROOT = os.path.join(BASE_DIR, "dockerfiles")
DOCKERS_PATH = os.path.join(DOCKERFILES_ROOT, "dockers.json")
DOCKERS = read_json(DOCKERS_PATH)

# source code snippets directory
SNIPPET_ROOT = BASE_DIR / "snippets_source"
