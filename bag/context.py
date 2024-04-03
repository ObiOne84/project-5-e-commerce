from decimal import Decimal
from django.conf import settings
from products.models import Comic, Book
from wishlist.models import Wishlist


def bag_content(request):

    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_items = request.user.wishlist.items.all()

    bag_items = []
    total = 0
    product_count = 0
    discount = 0
    vat = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        try:
            book = Book.objects.get(pk=item_id)
            product_type = 'book'
            product = book
        except Book.DoesNotExist:
            try:
                comic = Comic.objects.get(pk=item_id)
                product_type = 'comic'
                product = comic
            except Comic.DoesNotExist:
                return render(request, '404.html')

        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if product_count >= settings.DISCOUNT_THRESHOLD:
        discount = Decimal(total * settings.DISCOUNT_RATE) / 100

    if total < settings.FREE_DELIVERY_THRESHOLD and product_count > 0:
        delivery = settings.STANDARD_DELIVERY_CHARGE
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total - discount

    vat = Decimal(grand_total * settings.STANDARD_VAT_RATE / 100)

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'vat': vat,
        'discount': discount,
        'wishlist_items': wishlist_items,
    }

    return context
