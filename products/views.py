from django.shortcuts import render
from .models import Comic, Book

def all_products(request):
    """A view to display all products"""

    comics = Comic.objects.all()
    books = Book.objects.all()

    products = list(comics) + list(books)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

