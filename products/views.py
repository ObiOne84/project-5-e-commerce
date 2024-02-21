from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Comic, Book


def all_products(request):
    """A view to display all products"""

    comics = Comic.objects.all()
    books = Book.objects.all()
    products = list(comics) + list(books)
    total_products = len(products)
    is_paginated = len(products) > 24
    paginator = Paginator(products, 24)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'paginator': paginator,
        'is_paginated': is_paginated,
        'total_products': total_products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to display product details"""
    try:
        book = Book.objects.get(pk=product_id)
        product = book
        context = {'product': product, 'product_type': 'book'}
    except Book.DoesNotExist:
        try:
            comic = Comic.objects.get(pk=product_id)
            product = comic
            context = {'product': product, 'product_type': 'comic'}
        except Comic.DoesNotExist:
            return render(request, '404.html')  # or any other appropriate handling for non-existing products

    if product.subcategory.exists():
        subcategory = product.subcategory.first()  # Assuming each product has only one subcategory
        context['subcategory'] = subcategory
    
    return render(request, 'products/product_detail.html', context)
