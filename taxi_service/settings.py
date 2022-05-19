"""
Django settings for taxi_service project.
Generated by "django-admin startproject" using Django 4.0.2.
For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import json
from pathlib import Path

# Config
import dj_database_url

CONFIG_FILE = 'taxi_service/config.json'

# Build paths inside the project like this: BASE_DIR / "subdir".


BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_registration",
    "taxi",
    "rest_framework",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "taxi_service.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "taxi_service.wsgi.application"


# Password validation


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "taxi.Driver"

LOGIN_REDIRECT_URL = '/'

# Internationalization


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Kiev"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)


STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

with open(file=CONFIG_FILE, mode='r') as fin:
    config = json.load(fin)

    DEBUG = config.get("DEBUG", True)

    if DEBUG:
        INSTALLED_APPS.append('debug_toolbar')

    SECRET_KEY = config.get("SECRET_KEY", "django-insecure-8ovil3xu6=eaoqd#-#&ricv159p0pypoh5_lgm*)-dfcjqe=yc")

    ALLOWED_HOSTS = ["127.0.0.1"]

    if "HOSTS" in config:
        ALLOWED_HOSTS.append(config["HOSTS"])

    DATABASES = {
        "default": None
    }

    if config["PRODUCTION"]:
        DATABASES["default"] = dj_database_url.config(
            default="postgres://psclqdvh:7HJU3cp8P00cimDn4HigTSpfN9nC0MMW@abul.db.elephantsql.com/psclqdvh",
            conn_max_age=600)
    else:
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR / "db.sqlite3",
            }
        }


