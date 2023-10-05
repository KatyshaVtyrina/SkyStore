from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


# class ProductCreateView(CreateView):
#     model = Product
#     template_name = 'catalog/includes/product_detail.html'


# class ProductUpdateView(UpdateView):
#     model = Product
#     template_name = 'catalog/includes/product_detail.html'
#
#
# class ProductDelete(DeleteView):
#     model = Product
#     template_name = 'catalog/includes/product_detail.html'


def display_contacts(request):
    return render(request, 'catalog/contacts.html')
