from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from django.views import View
from django.contrib.auth.decorators import login_required
from itertools import chain

from .models import Comic, Book, Review, Subcategory
from .forms import ReviewForm, AddComicForm, AddBookForm


def all_products(request):
    """A view to display all products"""

    comics = Comic.objects.all()
    books = Book.objects.all()
    # products = list(comics) + list(books)
    products = list(Comic.objects.all()) + list(Book.objects.all())
    # products = list(comics) + list(books)

    # Source: Boutique Ado walkthrough project
    query = None
    # categories = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if query:
                queries = Q(title__icontains=query) | Q(author__icontains=query)
                comics = comics.filter(queries)
                books = books.filter(queries)
                # Source: https://stackoverflow.com/questions/46695150/django-search-fields-in-multiple-models
                products = list(chain(books, comics))
                if len(products) == 0:
                    messages.error(request, f"Sorry we didn't find any product matching '{query}'.")
                    return redirect(reverse('products'))
            else:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

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
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to display product details"""
    try:
        product = Book.objects.get(pk=product_id)
        product_type = 'book'
    except Book.DoesNotExist:
        try:
            product = Comic.objects.get(pk=product_id)
            product_type = 'comic'
        except Comic.DoesNotExist:
            return render(request, '404.html')  # or any other appropriate handling for non-existing products
            # You can change above line to the error message to display for the user.

    reviews = product.reviews.filter(approved=True).order_by('created_on')

    if request.method == 'POST':
        if request.user.is_authenticated:
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
            return HttpResponseForbidden("You must be logged in to submit a review.")
    else:
        form = ReviewForm()

    context = {
        'product': product,
        'product_type': product_type,
        'reviews': reviews,
        'review_form': form,
        'reviewed': False,
    }
    
    return render(request, 'products/product_detail.html', context)


class AddBook(View):
    """A view to allow site owner to add new products to catalogue"""

    def get(self, request, *args, **kwargs):
        book_form = AddBookForm()
        context = {
            'book_form': book_form,
        }
        return render(request, 'products/add_book.html', context)

    def post(self, request, *args, **kwargs):

        book_form = AddBookForm(request.POST, request.FILES)

        if book_form.is_valid():
            book = book_form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('product_detail', args=[book.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure form is valid.')
            context = {
                'book_form': book_form,
            }
            print(comic_form.errors)
            print(book_form.errors)
            return render(request, 'products/add_book.html', context)

class AddComic(View):
    """A view to add comic book"""

    def get(self, request, *args, **kwargs):
        comic_form = AddComicForm()
        context = {
            'comic_form': comic_form,
        }
        return render(request, 'products/add_comic.html', context)

    def post(self, request, *args, **kwargs):

        comic_form = AddComicForm(request.POST, request.FILES)

        if comic_form.is_valid():
            comic = comic_form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('product_detail', args=[comic.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure form is valid.')
            context = {
                'comic_form': comic_form,

            }
            print(comic_form.errors)

            return render(request, 'products/add_comic.html', context)


@login_required
def edit_book(request, product_id):
    """A view to update book"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can update products.')
        return redirect(reverse('home'))

    try:
        product = get_object_or_404(Book, pk=product_id)
        product_type = 'book'
    except Book.DoesNotExist:
        messages.error(request, 'The product you are looking for does not exist.')
        return render(request, '404.html')
    
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.title}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, f'Failed to update {product.title}. Please ensure the form is valid.')
    else:
        form = AddBookForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'product_type': product_type,
    }

    return render(request, template, context)


@login_required
def edit_comic(request, product_id):
    """A view to update comic"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can update product.')
        return redirect(reverse('home'))
 
    try:
        product = get_object_or_404(Comic, pk=product_id)
        product_type = 'comic'
    except Comic.DoesNotExist:
        messages.error(request, 'The product you are looking for does not exists.')
        return render(request, '404.html')
    
    if request.method == 'POST':

        form = AddComicForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.title}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, f'Failed to update {product.title}. Please ensure the form is valid.')
    else:
        form = AddComicForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'product_type': product_type,
    }

    return render(request, template, context)


@login_required
def delete_book(request, product_id):
    """Delete a product from the store"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can delete product.')
        return redirect(reverse('home'))
    
    try:
        product = get_object_or_404(Book, pk=product_id)
        product.delete()
        messages.success(request, f'Product {product.title} deleted!')
    except Book.DoesNotExist:
        messages.error(request, f"The {product.title} does not exist!")
    
    return redirect(reverse('products'))


@login_required
def delete_comic(request, product_id):
    """Delete a product from the store"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can delete product.')
        return redirect(reverse('home'))
    
    try:
        product = get_object_or_404(Comic, pk=product_id)
        product.delete()
        messages.success(request, f'Product {product.title} deleted!')
    except Comic.DoesNotExist:
        messages.error(request, f"The {product.title} does not exist!")
    
    return redirect(reverse('products'))




