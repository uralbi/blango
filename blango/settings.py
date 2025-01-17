from pathlib import Path
from configurations import Configuration
from configurations import values
import os
import dj_database_url
from datetime import timedelta

class Dev(Configuration):

  BASE_DIR = Path(__file__).resolve().parent.parent
  SECRET_KEY = 'django-insecure-+sn%dpa!086+g+%44z9*^j^q-u4n!j(#wl)x9a%_1op@zz2+1-'
  DEBUG = values.BooleanValue(True)
  ALLOWED_HOSTS = values.ListValue(["localhost", "0.0.0.0", ".codio.io"])
  
  AUTH_USER_MODEL = "blango_auth.User"
  PASSWORD_HASHERS = [
      'django.contrib.auth.hashers.Argon2PasswordHasher',
      'django.contrib.auth.hashers.PBKDF2PasswordHasher',
      'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
      'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
  ]

  # Application definition
  INSTALLED_APPS = [
      'blango_auth',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.sites',
      'django.contrib.staticfiles',
      'debug_toolbar',
      'rest_framework',
      'rest_framework.authtoken',
      'crispy_forms',
      'blog',
      'allauth',
      'allauth.account',
      'allauth.socialaccount',
      'allauth.socialaccount.providers.google',
      'drf_yasg',
      'django_filters',
      'versatileimagefield',
  ]

  SITE_ID = 1
  ACCOUNT_USER_MODEL_USERNAME_FIELD = None
  ACCOUNT_EMAIL_REQUIRED = True
  ACCOUNT_USERNAME_REQUIRED = False
  ACCOUNT_AUTHENTICATION_METHOD = "email"

  REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
    "DEFAULT_THROTTLE_CLASSES": [
            "blog.api.throttling.AnonSustainedThrottle",
            "blog.api.throttling.AnonBurstThrottle",
            "blog.api.throttling.UserSustainedThrottle",
            "blog.api.throttling.UserBurstThrottle",
        ],
    "DEFAULT_THROTTLE_RATES": {
        "anon_sustained": "500/day",
        "anon_burst": "10/minute",
        "user_sustained": "5000/day",
        "user_burst": "100/minute",
    },
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_FILTER_BACKENDS": [
            "django_filters.rest_framework.DjangoFilterBackend"
        ],
    "DEFAULT_FILTER_BACKENDS": [
            "django_filters.rest_framework.DjangoFilterBackend",
            "rest_framework.filters.OrderingFilter"
        ],
  }
  SIMPLE_JWT = {
        "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    }
  SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
            "Token": {"type": "apiKey", "name": "Authorization", "in": "header"},
            "Basic": {"type": "basic"},
        }
    }

  MIDDLEWARE = [
      'debug_toolbar.middleware.DebugToolbarMiddleware',
      'django.middleware.security.SecurityMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
      # 'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
  ]

  ROOT_URLCONF = 'blango.urls'

  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates'],
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

  WSGI_APPLICATION = 'blango.wsgi.application'


  # Database
  # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

  DATABASES = values.DatabaseURLValue(f"sqlite:///{BASE_DIR}/db.sqlite3")
  
#   DATABASES = {
#     "default": dj_database_url.config(default=f"sqlite:///{BASE_DIR}/db.sqlite3"),
#     "alternative": dj_database_url.config(
#         "ALTERNATIVE_DATABASE_URL",
#         default=f"sqlite:///{BASE_DIR}/alternative_db.sqlite3",
#     ),
#     }
#   DATABASES = {
#       'default': {
#           'ENGINE': 'django.db.backends.sqlite3',
#           'NAME': BASE_DIR / 'db.sqlite3',
#       }
#   }

  # Password validation
  # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

  ADMINS = [("Ben Shaw", "ben@example.com"), ("Leo Lucio", "leo@example.com")]
  #   DJANGO_ADMINS="Ben Shaw,ben@example.com;Leo Lucio,leo@example.com"
  LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "__ {levelname} {asctime} {module} {process:d} {thread:d} \n__ {message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M,", },
        },
    "handlers": {
        "console": {"class": "logging.StreamHandler", 
                    "stream": "ext://sys.stdout",
                    "formatter": "verbose", },
        # "mail_admins": {
        #     "level": "ERROR",
        #     "class": "django.utils.log.AdminEmailHandler",
        #     "filters": ["require_debug_false"], },
      },
    # logging to a file:
    # "handlers": {
    # "file": {"class": "logging.FileHandler", "filename": "/var/log/blango.log"},
    # }
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
            }
    }


  # Internationalization
  # https://docs.djangoproject.com/en/3.2/topics/i18n/

  LANGUAGE_CODE = 'en-us'

  TIME_ZONE = values.Value("UTC")

  USE_I18N = True

  USE_L10N = True

  USE_TZ = True


  # Static files (CSS, JavaScript, Images)
  # https://docs.djangoproject.com/en/3.2/howto/static-files/

  STATIC_URL = '/static/'
  MEDIA_ROOT = BASE_DIR / 'media'
  MEDIA_URL =  '/media/'
  
  # Default primary key field type
  # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

  DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
  
  INTERNAL_IPS = ["192.168.10.93"]

  X_FRAME_OPTIONS = 'ALLOW-FROM ' + os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io'
  CSRF_COOKIE_SAMESITE = None
  CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io']
  CSRF_COOKIE_SECURE = True
  SESSION_COOKIE_SECURE = True
  CSRF_COOKIE_SAMESITE = 'None'
  SESSION_COOKIE_SAMESITE = 'None'

  CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
  RISPY_TEMPLATE_PACK = "bootstrap5"
  EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
  ACCOUNT_ACTIVATION_DAYS = 7
  REGISTRATION_OPEN = True


class Prod(Dev):
  DEBUG = False
  SECRET_KEY = values.SecretValue()
