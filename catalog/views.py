from django.shortcuts import render

from catalog.models import Product


def display_home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Каталог',
    }
    return render(request, 'catalog/home.html', context)


def display_contacts(request):
    return render(request, 'catalog/contacts.html')


def display_product(request):
    return render(request, 'catalog/includes/inc_product.html')

