from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
from os import getenv
from dotenv import load_dotenv

# Replace the DATABASES section of your settings.py with this
tmpPostgres = urlparse(os.getenv("DATABASE_URL"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
# print(DEBUG)
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "django-crud-todoapp-37wd.onrender.com"]

CSRF_ALLOW_ORIGIN = "https://django-crud-todoapp-37wd.onrender.com"
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # LOCAL APPS
    "crudapp",
    # THIRD PARTY APPS
    "crispy_forms",
    "crispy_bootstrap5",
    "widget_tweaks",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "crud_settings.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
        },
    },
]

WSGI_APPLICATION = "crud_settings.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": tmpPostgres.path.replace("/", ""),
            "USER": tmpPostgres.username,
            "PASSWORD": tmpPostgres.password,
            "HOST": tmpPostgres.hostname,
            "PORT": 5432,
        }
    }
LOGIN_REDIRECT_URL = "note_list"
LOGOUT_REDIRECT_URL = "login"
LOGIN_URL = "login"
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Nairobi"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
# STATIC_URL = "/static/"

MEDIA_URL = "/media/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

VENV_PATH = os.path.dirname(BASE_DIR)

STATIC_ROOT = os.path.join(VENV_PATH, "static_root")

MEDIA_ROOT = os.path.join(VENV_PATH, "media_root")

# STATIC_ROOT = BASE_DIR / "productionfiles"

STATIC_URL = "static/"
# STATIC_URL = "/static/"
# # STATIC_ROOT = os.path.join(BASE_DIR, "static")
# # STATIC_ROOT = BASE_DIR / "static"
# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# STATICFILES_DIRS = ["/static/"]
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
