from django.urls import path

from catalog.apps import CatalogConfig

from catalog.views import (display_home, display_contacts, display_product)

app_name = CatalogConfig.name

urlpatterns = [
    path('', display_home, name='home'),
    path('contacts/', display_contacts, name='contacts'),
    path('product/<int:pk>', display_product, name='product')
]
