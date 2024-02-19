from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Comic, Book

def all_products(request):
    """A view to display all products"""

    comics = Comic.objects.all()
    books = Book.objects.all()
    products = list(comics) + list(books)
    total_products = len(products)
    is_paginated = len(products) > 18
    paginator = Paginator(products, 18)

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
