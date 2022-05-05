# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-24yc%y79uj2swqov&zvbh845_)krh@-e+wizcde8yy-g%+hj8a'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_library_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password2022',
    }
}