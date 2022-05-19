from .base import *

DEBUG = True
SECRET_KEY = "django-insecure-8ovil3xu6=eaoqd#-#&ricv159p0pypoh5_lgm*)-dfcjqe=yc"
ALLOWED_HOSTS = ["127.0.0.1"]


INSTALLED_APPS.append('debug_toolbar')


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

