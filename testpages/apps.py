from django.apps import AppConfig

# Настройка отображения названия приложения в админке


class TestPagesConfig(AppConfig):
    name = 'testpages'
    verbose_name = "Генератор QR кода"
