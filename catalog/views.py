from django.shortcuts import render


def display_home(request):
    return render(request, 'catalog/home.html')


def display_contacts(request):
    return render(request, 'catalog/contacts.html')
