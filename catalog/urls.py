from django.urls import path

from catalog.apps import CatalogConfig

from catalog.views import (display_contacts, display_product, ProductListView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', display_contacts, name='contacts'),
    path('product/<int:pk>', display_product, name='product')
]
