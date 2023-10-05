from django.urls import path

from catalog.apps import CatalogConfig

from catalog.views import (display_contacts, ProductListView, ProductDetailView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', display_contacts, name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product')
]
