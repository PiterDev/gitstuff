from django.apps import AppConfig
from django.core.exceptions import MultipleObjectsReturned

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

        def patched_get_app(self, request, provider, client_id=None):
            from allauth.socialaccount.models import SocialApp

            apps = self.list_apps(request, provider=provider, client_id=client_id)
            print("Apps fetched:", vars(apps[0]))  # Debug line  print
            if len(apps) > 1:
                visible_apps = [app for app in apps if not app.settings.get("hidden")]
                print("Visible apps:", visible_apps)  # Debug line
                if len(visible_apps) != 1:
                    raise MultipleObjectsReturned
                apps = visible_apps
            elif len(apps) == 0:
                raise SocialApp.DoesNotExist()
            return apps[0]

        DefaultSocialAccountAdapter.get_app = patched_get_app
