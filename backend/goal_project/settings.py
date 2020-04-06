"""
Django settings for goal_project project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os

#The backend foler
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#the overall project directory
PROJ_DIR = os.path.dirname(BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7&fl81gzy+ds=42!b&d7*4nclh6lk#z78h(yhn33z3#l-)*ics'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    
    #first party apps
    'accounts', #the api for holding accounts
    'goals',#main api
    'scores',

    #the rest framwork
    'rest_framework',
    #the token for session based authentication
    'rest_framework.authtoken',

    #installs related to user authentication
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth',
    'rest_auth.registration',

    #for crispy forms
    'crispy_forms',

    'django.contrib.sites',

    #to connect to the frontend SPA, webpack loader
    'webpack_loader',

    #Included Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'goal_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'goal_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

#for static styling files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'goal_project', 'static')]

#to prevent sending to email server after registration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#set the custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'

#for use with crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

#django allauth
#can change email verification down the road in production app
ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_EMAIL_REQUIRED = True

#The REST FRAMEWORK DICTIONARY
REST_FRAMEWORK = { #want to authenticate with both token authentication and session authentication
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2
}

#Django all-auth settings
#unique email
ACCOUNT_UNIQUE_EMAIL = True
#no username required for registration serializer
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
#email is required
ACCOUNT_EMAIL_REQUIRED = True
#email is required
ACCOUNT_EMAIL_REQUIRED = True
#no account usernname
ACCOUNT_USERNAME_REQUIRED = False
#authentication method is email
ACCOUNT_AUTHENTICATION_METHOD = 'email'


#the register serializer setting
REST_AUTH_REGISTER_SERIALIZERS = {'REGISTER_SERIALIZER':'accounts.api.serializers.CustomRegisterSerializer'}
REST_AUTH_SERIALIZERS = {'LOGIN_SERIALIZER': 'accounts.api.serializers.CustomLoginSerializer'}









#####################################################################################old code, authentication backend############################################

#defines the authentication backends. Uses the auth backend as well as the API
#AUTHENTICATION_BACKENDS = (
    #LOGIN THROUGH DJANGO ADMIN
#    "django.contrib.auth.backends.ModelBackend",
    #allauth specific authentication methods, such as login by e-mail
#    "allauth.account.auth_backends.AuthenticationBackend",
#)
#########################################################################################################################################################################

#NEEDS TO BE UPDATES LATER######################################################
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
REDIRECT_FIELD_NAME = '/'
#################################################################################

#set the site key to allow for the sites install to work
SITE_ID = 1

#settings for webpack loader, shows where the file is detailing changes in the frontend
WEBPACK_LOADER = {
    'DEFAULT':{
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(PROJ_DIR, 'frontend', 'webpack-stats.json')
    }
}

#sets the url to direct to if not logged in
LOGIN_URL = '/accounts/login/'