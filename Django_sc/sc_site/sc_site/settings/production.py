from .base import *

SECRET_KEY = 'django-insecure-*6^b_9ztmlefnjk8_2+e+0@jfw0z7p%xeu#nkjj33hob2km#!c'

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Django_pro',
        'USER': 'Django_pro_server',
        'PASSWORD': 'hK8X7C_(',
        'HOST': '192.168.101.137',
    }
}

DEBUG = True


ALLOWED_HOSTS = ['*']