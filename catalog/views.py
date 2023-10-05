from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


def display_contacts(request):
    return render(request, 'catalog/contacts.html')


def display_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'object': product
    }
    return render(request, 'catalog/includes/inc_product.html', context)

