DATABASES = {
    'default': {
        'NAME': 'django',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'django',
        'PASSWORD': 'django',
    },
    'other': {
        'NAME': 'django_other',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'django_other',
        'PASSWORD': 'django_other',
    }
}

SECRET_KEY = "django_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
)
