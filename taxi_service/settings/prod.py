from .base import *
import dj_database_url


DEBUG = False
ALLOWED_HOSTS = ["taxi-service-proj.herokuapp.com", '127.0.0.1']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ProductionDB",
        "USER": "psclqdvh ",
        "PASSWORD": "7HJU3cp8P00cimDn4HigTSpfN9nC0MMW",
        "HOST": "abul.db.elephantsql.com/psclqdvh",
        "PORT": 5432,

    }
}

DATABASES["default"] = dj_database_url.config(default="postgres://psclqdvh:7HJU3cp8P00cimDn4HigTSpfN9nC0MMW@abul.db.elephantsql.com/psclqdvh", conn_max_age=600)

