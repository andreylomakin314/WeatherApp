from django.contrib import admin
from .models import City

admin.site.register(City)    # регистрируем в админке модель города
