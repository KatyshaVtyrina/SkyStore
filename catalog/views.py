from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('title', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('title', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:home')

#
#
# class ProductDelete(DeleteView):
#     model = Product
#     template_name = 'catalog/includes/product_detail.html'


def display_contacts(request):
    return render(request, 'catalog/contacts.html')
