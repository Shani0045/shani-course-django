from pathlib import Path
import os
from decouple import config
from ast import literal_eval

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = literal_eval(config("ALLOWED_HOSTS"))

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # add third party apps here
    "corsheaders",
    # Add custom created apps here
    'home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shanicourse.urls'

TEMPLATE_NAME = "templates"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, TEMPLATE_NAME)],
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

WSGI_APPLICATION = 'shanicourse.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.'+config("DB_ENGINE"),
        'NAME': config("DB_NAME"),
        'USER': config("DB_USER"),
        'PASSWORD': config("DB_PASSWORD"),
        'HOST': config("DB_HOST"),
        'PORT': config("DB_PORT")
    }
}

# Retry the database connection until it's successful
# max_retries = 5
# retry_count = 0
# import psycopg2
# from psycopg2 import OperationalError
# from django.core.exceptions import ImproperlyConfigured

# while retry_count < max_retries:
#     try:
#         connection = psycopg2.connect(
#             dbname = config("DB_NAME"),
#             user = config("DB_USER"),
#             password = config("DB_PASSWORD"),
#             host = config("DB_HOST"),
#             port = config("DB_PORT"),
#         )
#         connection.close()
#         break  # Exit the loop when the connection is successful
#     except OperationalError as e:
#         print(f"Database connection error: {e}")
#         retry_count += 1

# if retry_count >= max_retries:
#     raise ImproperlyConfigured("Failed to connect to the database after multiple retries")


# Cors Configurations
CORS_ALLOWED_ORIGINS = literal_eval(config("CORS_ALLOWED_ORIGIN"))
CORS_ALLOW_METHODS = literal_eval(config("CORS_ALLOWED_METHODS"))
CORS_ALLOW_HEADERS = literal_eval(config("CORS_ALLOW_HEADERS"))
CORS_ALLOW_CREDENTIALS = config("CORS_ALLOW_CREDENTIALS", cast=bool)

CSRF_TRUSTED_ORIGINS = literal_eval(config("CSRF_TRUSTED_ORIGINS"))

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_DIR_NAME = "static"

STATIC_ROOT = os.path.join(BASE_DIR, STATIC_DIR_NAME)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configure the 404 handler
handler404 = 'home.views.custom_404_view'
