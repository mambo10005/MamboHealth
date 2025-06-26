from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# -- Recommended CodeRed Cloud settings ---------------------------------------

import os

ALLOWED_HOSTS = [os.environ['VIRTUAL_HOST']]

SECRET_KEY = os.environ['RANDOM_SECRET_KEY']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Built-in email sending service provided by CodeRed Cloud.
# Change this to a different backend or SMTP server to use your own.
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # or "optional"
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/login/"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "healthmambo@gmail.com"
EMAIL_HOST_PASSWORD = "evzncgosflndmnyh"
DEFAULT_FROM_EMAIL = "Mambo Health <healthmambo@gmail.com>"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ['DB_HOST'],
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'OPTIONS': {
            'client_encoding': 'UTF8',
            'sslmode': 'require',
        },
    }
}

