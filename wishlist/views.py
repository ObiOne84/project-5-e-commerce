from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.http import is_safe_url
from django.contrib import messages
from products.models import Product
from .models import Wishlist


@login_required
def view_wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_items = request.user.wishlist.items.all()
    quantity_range = range(1, 11)
    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
        'quantity_range': quantity_range,
    }
    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """View that allows users to add products to wishlist"""

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id is not None:
            try:
                product = Product.objects.get(pk=product_id)
                if not product.is_in_wishlist(request.user):
                    request.user.wishlist.items.add(product)
                    messages.success(
                        request, f'{product.title} successfully added \
                        to the Wishlist')
                    previous_url = request.META.get('HTTP_REFERER')
                    if previous_url and is_safe_url(
                            previous_url, allowed_hosts=request.get_host()):
                        return redirect(previous_url)
                    else:
                        return redirect(reverse('view_wishlist'))
                else:
                    messages.info(
                        request, f'{product.title} is already in your Wishlist'
                    )
                    pass
            except Product.DoesNotExist:
                messages.error(request, 'Sorry, we could not find the product \
                in our database')
                return redirect(reverse('products'))
                pass
    messages.error(request, 'Sorry, we could not find the product in \
    our database')
    return redirect('products')


@login_required
def remove_from_wishlist(request, product_id):
    """View that allows users to remove products from wishlist"""

    product = Product.objects.get(pk=product_id)
    if product.is_in_wishlist(request.user):
        request.user.wishlist.items.remove(product)
    messages.success(
        request, f'{product.title} successfully removed from the Wishlist')
    previous_url = request.META.get('HTTP_REFERER')

    if previous_url and is_safe_url(
            previous_url, allowed_hosts=request.get_host()):
        return redirect(previous_url)
    else:
        return redirect(reverse('view_wishlist'))
