#!/usr/bin/python
# -*- coding: utf-8 -*-
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys,locale
from pathlib import Path




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR =os.path.join(BASE_DIR,'templates')
#STATIC_DIR =os.path.join(BASE_DIR,'static')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bp%m!abw*9i(5w03ppawu9jyl0&if-l#++6n2enu41)xvnym@y'
STORE_ID='sumonben'
STORE_PASS="Sumon@747934"
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['209.74.88.131','localhost','gmrwc.edu.bd','www.gmrwc.edu.bd','gmrbwc.edu.bd','www.gmrbwc.edu.bd']

SESSION_COOKIE_AGE = 43000 # 3 minutes. "1209600(2 weeks)" by default 
SESSION_SAVE_EVERY_REQUEST = True # "False" by default
# Application definition

#AUTH_USER_MODEL='account.CustomUser'
AUTHENTICATION_BACKENDS = ['account.backends.EmailBackend']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'frontpage',
    'department',
    'ckeditor',
    'sortedm2m_filter_horizontal_widget',
    'import_export',
    'teacher',
    'student',
    'admission',
    'certificates',
    'payment',
    'employee',
    'rangefilter',
    'django_admin_listfilter_dropdown',
    'blog'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'gmrwc.urls'

X_FRAME_OPTIONS='SAMEORIGIN'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.posts',
            ],
        },
    },
]

WSGI_APPLICATION = 'gmrwc.wsgi.application'
LOGIN_REDIRECT_URL = '/account/profile/'
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'gmrbwc',
            'USER': 'postgres',
            'PASSWORD': 'Sumon@747934',
            'HOST': 'localhost',
            'PORT': '5432',
        }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
CKEDITOR_UPLOAD_PATH = "media/uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

# CKEditor Settings
 
CKEDITOR_CONFIGS = {
    'default':
        {
            'toolbar': 'full',
            'width': 'auto',
            'extraPlugins': ','.join([
                'codesnippet',
            ]),
        },
    'awesome_ckeditor': {
        'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline',
             '-', 'Link', 'Unlink', 'Anchor',
             '-', 'Format',
             
             '-', 'Maximize',
             
            ],
        ],  
        'width': 'auto',
        'toolbarCanCollapse': True,
        'height': 100,
    },
}
'''CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 200,
        'width': 'full',
        'toolbarCanCollapse': True,

    },
    'awesome_ckeditor': {
        'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline',
             '-', 'Link', 'Unlink', 'Anchor',
             '-', 'Format',
             
             '-', 'Maximize',
             
            ],
        ],  
        'width': 'auto',
        'toolbarCanCollapse': True,
        'height': 100,
    },
}
'''

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True



MEDIA_ROOT =  BASE_DIR / 'media' 
MEDIA_URL = '/media/'
STATIC_URL = 'static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static/')
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_ROOT='/home/gmrwcedubd/test.gmrwc.edu.bd/static/'
#MEDIA_ROOT =  BASE_DIR / 'media' 
# MEDIA_ROOT = "/home/gmrwcedubd/www.media.gmrwc.edu.bd/media/"
# MEDIA_URL = "https://www.media.gmrwc.edu.bd/media/"# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField/media/'
