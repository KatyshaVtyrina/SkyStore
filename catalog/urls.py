from django.urls import path

from catalog.apps import CatalogConfig

from catalog.views import display_home, display_contacts


app_name = CatalogConfig.name

urlpatterns = [
    path('', display_home),
    path('contacts/', display_contacts)
]
