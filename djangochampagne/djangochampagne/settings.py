"""
Django settings for djangochampagne project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# DATABASE_URL = "postgresql://postgres:DlXXkvUy13aGep9I8Bzw@containers-us-west-87.railway.app:6640/railway"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6s1^qd*qom^$i6js$=az+85my)czdh8%t)vk&e)@si=c3urwpf'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = []

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'static','media')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'crispy_forms',
    'crispy_bootstrap4',
    'stripe'
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

ROOT_URLCONF = 'djangochampagne.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.menu_links',
                'store.context_processors.counter'
            ],
        },
    },
]

WSGI_APPLICATION = 'djangochampagne.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'store', 
        'USER': 'root',
        'PASSWORD': 'root1',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('railway'), 
#         'USER': os.getenv('postgres'),
#         'PASSWORD': os.getenv('DlXXkvUy13aGep9I8Bzw'),
#         'HOST': os.getenv('containers-us-west-87.railway.app'),
#         'PORT': os.getenv('6640')
#     }
# }

# DATABASES = {
#     'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800)
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
CRISPY_TEMPLATE_PACK = 'Bootstrap4'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PUBLIC_KEY='pk_test_51NP2bQDJvYmYe7OnmIJRrEpP37mkDGBLRqJ6sAldqLO8SbTBm3ZQLSzLVEURZ40oYwjZmagZDJJx33vva8tewljy007rsVLrom'
SECRET_KEY='sk_test_51NP2bQDJvYmYe7OneXwKTjOOTTzSB8N5a7rpt3PUkjeo8NuwoHbRjUpvDFggy8AXhLtEqjzJw3vF8405tFyjbluL007OEIbslc'
