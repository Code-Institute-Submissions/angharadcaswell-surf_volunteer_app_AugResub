from django.apps import AppConfig


class VolunteerDashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'volunteer_dashboard'


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals  # noqa
