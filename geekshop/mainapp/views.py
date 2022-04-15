
from django.shortcuts import render
def main(request):
    context = {'no' : 'oh no'}
    return render(request, 'mainapp/index.html', context=context)


def products(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    context = {'links_menu': links_menu}

    return render(request, 'mainapp/products.html', context=context)


def products_all(request):
    return render(request, 'mainapp/products_all.html')

def contact(request):
    return render(request, 'mainapp/contact.html')