from .base import *
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = False
ALLOWED_HOSTS = ["taxi-service-proj.herokuapp.com", '127.0.0.1', "https://taxi-service-proj.herokuapp.com/"]



DATABASES = {
    "default": None
}

DATABASES["default"] = dj_database_url.config(default="postgres://psclqdvh:7HJU3cp8P00cimDn4HigTSpfN9nC0MMW@abul.db.elephantsql.com/psclqdvh", conn_max_age=600)

