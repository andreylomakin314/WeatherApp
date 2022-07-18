from django.apps import AppConfig


class WeatherConfig(AppConfig):
    """Сохраняем метаданные в экземпляре"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'
