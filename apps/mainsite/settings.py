import sys
import os

from mainsite import TOP_DIR


##
#
#  Important Stuff
#
##

INSTALLED_APPS = [
    # https://github.com/concentricsky/django-client-admin
    'client_admin',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'reversion',
    'ckeditor',
    'south',
    'jingo',
    'djangosphinx',
    'skycms.structure',
    'sky_thumbnails',
    'ckeditor',
    'sky_redirects',
    'emailtemplates',
    'sky_visitor',

    'mainsite',
    'homepage',
    'search',

    'rest_framework',
    'data',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mainsite.middleware.MaintenanceMiddleware',
    # 'mainsite.middleware.TrailingSlashMiddleware',
]

ROOT_URLCONF = 'mainsite.urls'

SECRET_KEY = '{{secret_key}}'

# Hosts/domain names that are valid for this site.
# "*" matches anything, ".example.com" matches example.com and all subdomains
ALLOWED_HOSTS = ['*', ]

ALLOW_SLASH = True

##
#
#  Templates
#
##

TEMPLATE_LOADERS = [
    'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

TEMPLATE_DIRS = [
    os.path.join(TOP_DIR, 'breakdown', 'templates'),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
]

JINGO_EXCLUDE_APPS = (
    'admin',
    'registration',
    'debug_toolbar',
    'ckeditor',
    'reversion',
    'rest_framework',
    )


##
#
#  Static Files
#
##

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_ROOT = os.path.join(TOP_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(TOP_DIR, 'breakdown', 'static'),
]


##
#
#  Media Files
#
##

MEDIA_ROOT = os.path.join(TOP_DIR, 'mediafiles')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = STATIC_URL+'admin/'


##
#
#   Fixtures
#
##

FIXTURE_DIRS = [
    os.path.join(TOP_DIR, 'etc', 'fixtures'),
]


##
#
#  Logging
#
##

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': [],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


##
#
#  Maintenance Mode
#
##

MAINTENANCE_MODE = False
MAINTENANCE_URL = '/maintenance'


##
#
#  Sphinx Search
#
##

SPHINX_API_VERSION = 0x116 # Sphinx 0.9.9


##
#
#  CKEditor
#
##

# https://github.com/concentricsky/django-sky-ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            [      'Undo', 'Redo',
              '-', 'Format',
              '-', 'Bold', 'Italic', 'Underline',
              '-', 'Link', 'Unlink',
              '-', 'BulletedList', 'NumberedList',
            ],
            [      'SpellChecker', 'Scayt',
            ],
            [      'Image',
              '-', 'PasteText','PasteFromWord',
              '-', 'Source',
            ]
        ],
        'contentsCss': STATIC_URL+'css/ckeditor.css',
        'format_tags': 'p;h3;h4',
        'width': 655,
        'height': 250,
        'toolbarCanCollapse': False,
        'debug': True,
        'linkShowTargetTab': False,
        'linkShowAdvancedTab': False,
    }
    , 'basic': {
        'toolbar': [
            [      'Bold', 'Italic',
              '-', 'Link', 'Unlink',
            ]
        ]
        , 'width': 600
        , 'height': 250
        , 'toolbarCanCollapse': False
        , 'toolbarLocation': 'bottom'
        , 'resize_enabled': False
        , 'removePlugins': 'elementspath'
        , 'forcePasteAsPlainText': True
    }
}

CKEDITOR_EMBED_CONTENT = ['structure.page', 'structure.fileupload', 'blog.post']


##
#
#  Misc.
#
##

SITE_ID = 1

USE_I18N = False
USE_L10N = False
USE_TZ = True


##
#
#  Django Rest Framework
#
##

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

##
#
#  Import settings_production and settings_local.
#
##

try:
    from settings_production import *
except ImportError as e:
    pass

try:
    from settings_local import *
except ImportError as e:
    import sys
    sys.stderr.write("no settings_local found, setting DEBUG=True...\n")
    DEBUG = True
    pass
