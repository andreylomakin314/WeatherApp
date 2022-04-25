DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sqlite3',
        'USER': 'andrey',
        'PASSWORD': '123123',
        'HOST': 'localhost',
        'PORT': '5432',
    }