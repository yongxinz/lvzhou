#!/usr/bin/env python
# coding=utf-8

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lvzhou',
    }
}

INSTALLED_APPS += [
    'rest_framework',
]
