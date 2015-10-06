"""
Django settings for clubwebsystem project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
from django.contrib import messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Restrict connections to a list of hosts
ALLOWED_HOSTS = []

# Must set some secret key initially, to avoid errors when importing the settings module
# into other settings sub-files (s_40_development.py, etc.)
SECRET_KEY = '00000000000000000000000000000000000000000000000000'

# Application definition
INSTALLED_APPS = [
  # bootstrap the admin (must be before django.contrib.admin)
  'django_admin_bootstrapped',
  # django
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.sites',
  'django.contrib.staticfiles',
  # third party apps
  'crispy_forms',
  'registration',
  'versatileimagefield',
  # our own
  'clubdata',
  'clubmembers',
  'contentblocks',
  'events',
  'mainsite',
  'regbackend',
]

# Middleware
MIDDLEWARE_CLASSES = (
  # django
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'django.middleware.security.SecurityMiddleware',
  # third party middleware
  # our own
)

# URL settings
ROOT_URLCONF = 'clubwebsystem.urls'

# Templates
TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, "templates")],
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

# Custom user model
AUTH_USER_MODEL = 'clubmembers.Member'
AUTHENTICATION_BACKENDS = ('clubmembers.models.MemberAuthenticationBackend',)

# Which python module will the WSGI server load
WSGI_APPLICATION = 'clubwebsystem.wsgi.application'

# Settings for django.sites
SITE_ID = 1

# Internationalization
USE_I18N = False
USE_L10N = False
USE_TZ = False
DATE_FORMAT = 'N j, Y' # Default date format when displaying dates in templates

# Static files (CSS, JavaScript, Images). Because we're using try_files
# in nginx, we serve static content from the same URI root that the pages
# are in. For development, we can override this with '/static/'.
STATIC_URL = '/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "static_root")
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, "static"),
)

# Media files (untrusted files uploaded by users)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "media_root")

# CSS styles for various messages (django.contrib.messages framework)
MESSAGE_TAGS = {
  messages.INFO: 'alert-info',
  messages.SUCCESS: 'alert-success',
  messages.WARNING: 'alert-warning',
  messages.ERROR: 'alert-danger'
}

#Crispy FORM TAGs SETTINGS
CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG

#DJANGO REGISTRATION REDUX SETTINGS
REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 2

# Django auth settings
LOGIN_REDIRECT_URL = '/'

# Settings for django-versatileimagefield
VERSATILEIMAGEFIELD_SETTINGS = {
  'cache_length': 2592000,
  'cache_name': 'versatileimagefield_cache',
  'jpeg_resize_quality': 70,
  'sized_directory_name': '__sized__',
  'filtered_directory_name': '__filtered__',
  'placeholder_directory_name': '__placeholder__',
  'create_images_on_demand': True
}
