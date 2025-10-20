# erp_system/settings_prod.py
from .settings import *
import os

# Security
DEBUG = False
ALLOWED_HOSTS = ['erp.fattahinfotech.com', 'www.erp.fattahinfotech.com', 'root@72.60.208.8']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'erp_system',
        'USER': 'erp_user',
        'PASSWORD': 'deploy@1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = False  # Set to True after SSL setup
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Email (configure based on your email service)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'support@fattahinfotech.com'
EMAIL_HOST_PASSWORD = '12345678'