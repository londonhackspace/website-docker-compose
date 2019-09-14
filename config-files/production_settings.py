from .settings import *

# SECURITY WARNING: create your own key, and keep it secret!
SECRET_KEY = ')(umc97y$zy@=_4y1ca3(rrxr1n=9#27ikx#$67@95!j-p^zfy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SITE_ID = 1
DOMAIN_NAME = 'london.hackspace.org.uk'
ABSOLUTEURI_PROTOCOL = 'https'

ALLOWED_HOSTS = [DOMAIN_NAME]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'db',
        'NAME': 'hackspace',
        'USER': 'hackspace',
        'PASSWORD': 'hackspace',
    }
}

PROJECT_MAILING_LIST = 'london-hack-space-test'

FLOURISH_LOOPBACK_URLS = {
    'authenticate': 'https://nginx/session.php',
    'destroy': 'https://nginx/session.php?destroy',
}

CONTACT_EMAIL = 'contact@' + DOMAIN_NAME
NOREPLY_EMAIL = 'no-reply@' + DOMAIN_NAME

