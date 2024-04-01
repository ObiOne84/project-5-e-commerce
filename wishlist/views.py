from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from products.models import Product
from .models import Wishlist


@login_required
def view_wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_items = request.user.wishlist.items.all()
    template = 'wishlist/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
    }
    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """View that allows users to add products to wishlist"""
    product = Product.objects.get(pk=product_id)
    if not product.is_in_wishlist(request.user):
        request.user.wishlist.items.add(product)

    return redirect('wishlist/wishlist.html')


@login_required
def remove_from_wishlist(request, product_id):
    product = Product.objects.get(pk=product_id)
    if product.is_in_wishlist(request.user):
        request.user.wishlist.items.remove(product)
    return redirect('wishlist/wishlist.html')
