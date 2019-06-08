import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

ALLOWED_HOSTS = ['celianon.pythonanywhere.com']

SECRET_KEY = 'o7yo95^hy3-_c*#!m+m&^nc_t=!(@17mw6p1_@s)&s27njp_v$'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'mydatabase'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST': '127.0.0.1',
#         'NAME': 'djangotest',
#         'USER': 'root',
#         'PASSWORD': '',
#         'PORT': ''
#     }
# }

STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
