import os
from pathlib import Path
import environ
from datetime import timedelta
import dj_database_url
from decouple import config
import socket

IS_LOCAL = socket.gethostname() == 'localhost' or os.getenv("ENV") == "local"

SECRET_KEY = os.getenv('SECRET_KEY', 'un_valor_por_defecto_seguro')  # Configúrala en Render

BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    'apps.users',
    'apps.habito',
    'apps.hydration',
    'apps.dailyProgress',
    'apps.userActivity',
    'apps.reminder',
    'apps.generalLogs',
    'apps.adminLogs',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ¡Debe estar arriba de SecurityMiddleware!
    'corsheaders.middleware.CorsMiddleware',
    # 'apps.auth.middleware.ClerkJWTAuthenticationMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env')) 

DATABASES = {
    'default': dj_database_url.parse(
        "postgresql://postgres.yzdohosbanqdbezyyrwv:XgX*kf+98Szq4B@aws-0-us-east-2.pooler.supabase.com:5432/postgres?sslmode=require",
        conn_max_age=600
    )
}

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

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'apps.authentication.clerk_authentication.ClerkJWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

CLERK_JWKS_URL = "https://curious-mammoth-54.clerk.accounts.dev/.well-known/jwks.json"
CLERK_ISSUER = "https://curious-mammoth-54.clerk.accounts.dev"
CLERK_AUDIENCE = "https://backend-app-habitos.onrender.com"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://*.supabase.co",
    "https://*.onrender.com",
]

DEBUG = False  # Siempre False en producción
ALLOWED_HOSTS = ['*'] 

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CORS_ALLOW_ALL_ORIGINS = True 

CORS_ALLOW_CREDENTIALS = True

# Configuración de seguridad
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
