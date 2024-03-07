from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from django.views import View
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.db.models.functions import Lower
from django.db.models import F

from .models import Comic, Book, Review, Subcategory, Category
from .forms import ReviewForm, AddComicForm, AddBookForm


def all_products(request):
    """A view to display all products, with sorting and filetring"""
    # changed all union to list(chain)
    comics = Comic.objects.all()
    books = Book.objects.all()
    # Source: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#union
    products = list(chain(comics, books))
    # products = comics.union(books)
    category = Category.objects.all()
    # Source: Boutique Ado walkthrough project
    query = None
    categories = None
    sort = None
    direction = None


    if request.GET:           
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            if categories == ['books']:
                products = books
                messages.success(request, "You are viewing results for 'all books'")
            elif categories == ['comics']:
                products = comics
                messages.success(request, "You are viewing results for 'all comic books'")
            else:
                comics = comics.filter(category__name__in=categories)
                books = books.filter(category__name__in=categories)
                # products = comics.union(books)
                products = list(chain(comics, books))
                categories = Category.objects.filter(name__in=categories)
                category_display_names = ', '.join(category.display_name for category in categories)
                if len(products) > 0:
                    messages.success(request, f"You are viewing results for '{category_display_names}'")
                else:
                   messages.error(request, f"Sorry, there is not results for '{category_display_names}'")
                   return redirect(reverse('products'))
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'category':
                    books = books.annotate(category_name=Lower('category__name')).exclude(category__isnull=True)
                    comics = comics.annotate(category_name=Lower('category__name')).exclude(category__isnull=True)
                    products = list(chain(comics, books))
                    if 'direction' in request.GET:
                        direction = request.GET['direction']
                        if direction == 'asc' or direction is None:
                            products = sorted(products, key=lambda x: x.category_name)
                        else:
                            products = sorted(products, key=lambda x: x.category_name, reverse=True)
            elif sortkey == 'name':
                    sortkey = 'title'
                    # Annotate both querysets with a common field name for title
                    books = books.annotate(product_title=Lower('title'))
                    comics = comics.annotate(product_title=Lower('title'))
                    # Combine the annotated querysets
                    products = list(chain(comics, books))
                    if 'direction' in request.GET:
                        direction = request.GET['direction']
                        # Sort the combined queryset by title
                        if direction == 'asc' or direction is None:
                            products = sorted(products, key=lambda x: x.product_title)
                        else:
                            products = sorted(products, key=lambda x: x.product_title, reverse=True)
            elif sortkey == 'price':
                    # Annotate both querysets with a common field name for price
                    books = books.annotate(product_price=F('price'))
                    comics = comics.annotate(product_price=F('price'))
                    # Combine the annotated querysets
                    products = list(chain(comics, books))
                    if 'direction' in request.GET:
                        direction = request.GET['direction']
                        # Sort the combined queryset by price
                        if direction == 'asc' or direction is None:
                            products = sorted(products, key=lambda x: x.product_price)
                        else:
                            products = sorted(products, key=lambda x: x.product_price, reverse=True)
            elif sortkey == 'rating':
                    # Annotate both querysets with a common field name for rating
                    books = books.annotate(product_rating=F('rating'))
                    comics = comics.annotate(product_rating=F('rating'))
                    # Combine the annotated querysets
                    products = list(chain(comics, books))
                    if 'direction' in request.GET:
                        direction = request.GET['direction']
                        # Sort the combined queryset by rating
                        if direction == 'asc' or direction is None:
                            products = sorted(products, key=lambda x: x.product_rating)
                        else:
                            products = sorted(products, key=lambda x: x.product_rating, reverse=True)
            #     if 'direction' in request.GET:
            #         direction = request.GET['direction']
            #         if direction == 'desc':
            #             sortkey = f'-{sortkey}'
            #     products = products.order_by(sortkey)
        if 'q' in request.GET:
            query = request.GET['q']
            if query:
                queries = Q(title__icontains=query) | Q(author__icontains=query)
                comics = comics.filter(queries)
                books = books.filter(queries)
                product = list(chain(comics, books))
                # products = comics.union(books)
                # print('LINE 78: ', products)
                if len(products) == 0:
                    messages.error(request, f"Sorry we didn't find any product matching '{query}'.")
                    return redirect(reverse('products'))
            else:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

    current_sorting = f'{sort}_{direction}'
    print(current_sorting)

    products_list = list(products)
    total_products = len(products_list)
    # is_paginated = total_products > 18
    paginator = Paginator(products, 18)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    is_paginated = paginator.count > 18

    context = {
        # 'products': page_obj,
        'page_obj': page_obj,
        'paginator': paginator,
        'is_paginated': is_paginated,
        'total_products': total_products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        category: category,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to display product details and handle review functionality"""
    try:
        product = Book.objects.get(pk=product_id)
        product_type = 'book'
    except Book.DoesNotExist:
        try:
            product = Comic.objects.get(pk=product_id)
            product_type = 'comic'
        except Comic.DoesNotExist:
            return render(request, '404.html')
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
    """A view to allow site owner to add new book to catalogue"""

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
    """A view to add comic book to catalogue"""

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
    """Delete a book from the store"""

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
    """Delete a comic from the store"""

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




