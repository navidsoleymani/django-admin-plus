from pathlib import Path
import logging
import dotenv
import os

from .base import (
    installedApps,
)

dotenv.load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development conf - unsuitable for production
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = [
    '*',
]

# Application definition
INSTALLED_APPS = installedApps

# Middleware definition
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Base URL Root
ROOT_URLCONF = 'conf.urls'

# Template Conf
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
        },
    },
]

# WSGI Conf
WSGI_APPLICATION = 'conf.wsgi.application'

# Database
if os.environ.get('DEPLOY') == 'True':
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DATABASES_ENGINE'),
            'NAME': os.environ.get('DATABASES_NAME'),
            'USER': os.environ.get('DATABASES_USER'),
            'PASSWORD': os.environ.get('DATABASES_PASSWORD'),
            'HOST': os.environ.get('DATABASES_HOST'),
            'PORT': os.environ.get('DATABASES_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
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
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'files')

# Media files (Images, Videos, Voices, Documents)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS Conf
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOWED_ORIGINS = []
CORS_ALLOW_CREDENTIALS = True

# Logger Conf
logging.basicConfig(
    level=logging.DEBUG,
    # filename='.log',
    filemode='w',
    format='log: %(levelname)s - %(asctime)s - module: %(module)s - line number: %(lineno)d  - message: %(message)s'
)

# DRF Conf
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5
}
