from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Comic, Book, Review
from .forms import ReviewForm


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
        product_type = 'book'
        # product = book
        # reviews = product.reviews.filter(
        #     approved=True).order_by('created_on')

        # context = {
        #     'product': product,
        #     'product_type': 'book',
        #     'reviews': reviews,
        #     'reviewed': False,
        # }
    except Book.DoesNotExist:
        try:
            product = Comic.objects.get(pk=product_id)
            product_type = 'comic'
            # product = comic
            # reviews = product.reviews.filter(
            # approved=True).order_by('created_on')

            # context = {
            #     'product': product,
            #     'product_type': 'comic',
            #     'reviews': reviews,
            #     'reviewed': False,}
        except Comic.DoesNotExist:
            return render(request, '404.html')  # or any other appropriate handling for non-existing products

    reviews = product.reviews.filter(approved=True).order_by('created_on')

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.email = request.user.email
            form.instance.name = request.user.username
            review = form.save(commit=False)
            review.product = product
            review.save()
            messages.success(request, 'Review submitted successfully.')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'product_type': product_type,
        'reviews': reviews,
        'review_form': form,
        'reviewed': False,
    }

    if product.subcategory.exists():
        subcategory = product.subcategory.first()  # Assuming each product has only one subcategory
        context['subcategory'] = subcategory
    
    return render(request, 'products/product_detail.html', context)
