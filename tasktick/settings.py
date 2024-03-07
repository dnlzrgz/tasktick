"""
Django settings for tasktick project.
"""

from pathlib import Path
from environs import Env

# Load env variables
env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Keep the secret key used in production secret!
SECRET_KEY = env.str(
    "DJANGO_SECRET_KEY",
    "django-insecure-n_$ygen%espc=9o3mr62%y3h7)2)egdlzmd+-j49d9!lnnxbt2",
)

# Don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", [])


# Application definition

INSTALLED_APPS = [
    # 1st party
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # local
    "accounts",
    "activities",
    "projects",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tasktick.urls"

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

WSGI_APPLICATION = "tasktick.wsgi.application"

# Cache
# https://docs.djangoproject.com/en/5.0/ref/settings/#cache

CACHES = {
    "default": {
        "BACKEND": env.str(
            "CACHE_BACKEND",
            "django.core.cache.backends.dummy.DummyCache",
        ),
        "LOCATION": env.str("CACHE_URL", ""),
    }
}


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": env.str("DATABASE_ENGINE", "django.db.backends.sqlite3"),
        "NAME": env.path("DATABASE_NAME", BASE_DIR / "db.sqlite3"),
        "USER": env.str("DATABASE_USER", ""),
        "PASSWORD": env.str("DATABASE_PASSWORD", ""),
        "HOST": env.str("DATABASE_HOST", ""),
        "PORT": env.str("DATABASE_PORT", ""),
    }
}

DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

SITE_ID = 1

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# User model

AUTH_USER_MODEL = "accounts.CustomUser"

LOGIN_REDIRECT_URL = env.str("LOGIN_REDIRECT_URL", "home")
ACCOUNT_LOGOUT_REDIRECT_URL = env.str("LOGOUT_REDIRECT_URL", "home")
