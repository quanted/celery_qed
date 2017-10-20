"""
Django settings for sam celery

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sys

print('settings.py')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_ROOT = os.path.join(PROJECT_ROOT, 'templates_qed/') #.replace('\\','/'))
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_qed')
#os.path.join(PROJECT_ROOT, 'templates_qed')

try:
#    SECRET_KEY= os.environ.get('DOCKER_SECRET_KEY')
    with open('secret_key_django_dropbox.txt') as f:
        SECRET_KEY = f.read().strip()
except:
    print("Secret file not set as env variable")
    #SECRET_KEY = 'Shhhhhhhhhhhhhhh'

IS_PUBLIC = False

ADMINS = (
    ('Tom Purucker', 'purucker.tom@epa.gov'),
    ('Kurt Wolfe', 'wolfe.kurt@epa.gov'),
)

APPEND_SLASH = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(TEMPLATE_ROOT, 'splash'),
                 # os.path.join(TEMPLATE_ROOT, 'drupal_2017'),
                 # os.path.join(TEMPLATE_ROOT, 'cts'),
                 # os.path.join(TEMPLATE_ROOT, 'drupal_2014'),
                 # os.path.join(TEMPLATE_ROOT, 'uber2017'),
                 # os.path.join(TEMPLATE_ROOT, 'uber2011'),
                 # os.path.join(TEMPLATE_ROOT, 'hwbi'),
                 # ],
        # 'APP_DIRS': True,
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

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
    #'mod_wsgi.server',  # Only needed for mod_wsgi express (Python driver for Apache) e.g. on the production server
    # 'docs',
    # 'rest_framework_swagger',
    # 'splash_app',  # splash django app
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# ROOT_URLCONF = 'urls'



# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}


# Setups databse-less test runner (Only needed for running test)
#TEST_RUNNER = 'testing.DatabaselessTestRunner'

# CACHE Setup - required to run Django "sessions" without a database

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake'
#     }
# }
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static_qed'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATIC_URL = '/static_qed/'

#print('BASE_DIR = %s' %BASE_DIR)
print('PROJECT_ROOT = %s' %PROJECT_ROOT)
print('TEMPLATE_ROOT = %s' %TEMPLATE_ROOT)
#print('STATIC_ROOT = %s' %STATIC_ROOT)

# Path to Sphinx HTML Docs
# http://django-docs.readthedocs.org/en/latest/

DOCS_ROOT = os.path.join(PROJECT_ROOT, 'docs', '_build', 'html')
DOCS_ACCESS = 'public'
