from django.urls import path

from catalog.apps import CatalogConfig

from catalog.views import (display_contacts, ProductListView, ProductDetailView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    # path('create/<int:pk>', ProductCreateView.as_view(), name='create'),
    # path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('contacts/', display_contacts, name='contacts')
]
