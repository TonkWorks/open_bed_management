
""" Open Bed Management Settings
"""

from django.core.urlresolvers import reverse_lazy
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'app', 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'app', 'media')
MEDIA_URL = "/media/"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.setdefault("SECRET_KEY", '1e9+e*f-@ava1p@)40v)pr+v+ho=(21-kb=1w=zvcn@3#q7z^f')
ALLOWED_HOSTS = os.environ.setdefault("ALLOWED_HOSTS", '.tonkworks.com')

ALLOWED_HOSTS = ['localhost', ALLOWED_HOSTS]
DEBUG = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'dry_rest_permissions',
    'crispy_forms',
    'easy_thumbnails',
    'authtools',
    'profiles',
    'accounts',
    'rest_framework.authtoken',

    'constance',
    'constance.backends.database',
    'website',
    'beds',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'constance.context_processors.config',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_csv.renderers.CSVRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
        'rest_framework_yaml.renderers.YAMLRenderer',
        'website.renderers.Hl7Renderer'

    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated', # Require login for all of API
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_LIMIT': 25
}


PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    }
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True
CONSTANCE_CONFIG = {
    'SITE_NAME': ('Open Bed Management', 'Website Name'),
    'ALLOW_EMAIL_ALERTS': (True, 'Should users be able to subscribe to e-mail alerts')
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static2'

# Crispy Form Theme - Bootstrap 3
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# For Bootstrap 3, change error alert to 'danger'
from django.contrib import messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Authentication Settings
AUTH_USER_MODEL = 'authtools.User'
LOGIN_REDIRECT_URL = reverse_lazy("home")
LOGIN_URL = reverse_lazy("accounts:login")

THUMBNAIL_EXTENSION = 'png'     # Or any extn for your thumbnails

MANAGEPY = False

if os.environ.setdefault("APP_PRODUCTION", "") == "":
    MANAGEPY = True
    ES_HOST = 'localhost'
    #TRANSCRIBE_SYNC = True
    DEBUG = True  # True

    # Debug toolbar 
    INTERNAL_IPS = ('localhost', '127.0.0.1')
    INSTALLED_APPS += (
        'debug_toolbar.apps.DebugToolbarConfig',)
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    CONFIG_DEFAULTS = {
        'INTERCEPT_REDIRECTS': False,
    }
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]
    def show_toolbar(request):
        return True
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    }

# Email

ADMIN_EMAIL = os.environ.setdefault("ADMIN_EMAIL", "")

ADMINS = (
    ('', ADMIN_EMAIL),
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.environ.setdefault("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.environ.setdefault("EMAIL_USE_TLS", "587"))
EMAIL_USE_TLS = os.environ.setdefault("EMAIL_USE_TLS", True)

EMAIL_HOST_USER = os.environ.setdefault("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.setdefault("EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = os.environ.setdefault("DEFAULT_FROM_EMAIL", "")
DEFAULT_TO_EMAIL = os.environ.setdefault("DEFAULT_TO_EMAIL", "")
