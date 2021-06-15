from .base import *

STATIC_ROOT = '/home/dva_api/public_html/static'
MEDIA_ROOT = '/home/dva_api/public_html/media'

DEBUG = env('DEBUG')
ALLOWED_HOSTS = env('ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USERNAME'),
        'PASSWORD': env('PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_PORT = 2525
EMAIL_USE_TLS = False
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
