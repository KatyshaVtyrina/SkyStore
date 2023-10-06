from django.urls import path

from catalog.apps import CatalogConfig

from catalog.views import (display_contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView, PostListView, PostDetailView, PostCreateView, PostUpdateView,
                           PostDeleteView)

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),

    path('contacts/', display_contacts, name='contacts'),

    path('blog/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('post/create/', PostCreateView.as_view(), name='create_post'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='update_post'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='delete_post')
]
