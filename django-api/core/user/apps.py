from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # name = 'user'
    # label = 'user'
    name = 'core.user'
    label = 'core_user'
