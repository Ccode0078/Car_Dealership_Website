"""
Django settings for dealership project.
Django 5.1.x
"""

from pathlib import Path
import os

# --- Paths
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Security
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-uo6+*z82(ljee5dabqr2!le)i%g8^q=$img9w&&$cz61(xb_of",
)

# Default to DEBUG=True for local dev; override with DJANGO_DEBUG=False in prod.
DEBUG = os.getenv("DJANGO_DEBUG", "True").lower() == "true"

ALLOWED_HOSTS = ["127.0.0.1", "localhost", ".vercel.app", "car-dealership-website-two.vercel.app"]

# If you deploy behind HTTPS on Vercel, this helps with CSRF on that domain.
CSRF_TRUSTED_ORIGINS = [
    "https://*.vercel.app",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

# --- Apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "listings",
]

# --- Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dealership.urls"

# --- Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Look in a top-level /templates directory (in addition to app templates)
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

WSGI_APPLICATION = "dealership.wsgi.application"

# --- Database (SQLite for dev)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --- Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- I18N
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --- Static files (your CSS/JS/images that ship with the app)
STATIC_URL = "/static/"
# During development, Django serves files from these directories:
STATICFILES_DIRS = [BASE_DIR / "static"]
# For production collectstatic (e.g., Vercel build output target):
STATIC_ROOT = BASE_DIR / "staticfiles"

# --- Media files (user-uploaded; e.g., ImageField)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# --- Misc
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

