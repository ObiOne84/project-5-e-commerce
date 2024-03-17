from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages

from products.models import Book, Comic


def view_bag(request):
    """ A view to renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""

    try:
        product = Book.objects.get(pk=item_id)
        product_type = 'book'
    except Book.DoesNotExist:
        try:
            product = Comic.objects.get(pk=item_id)
            product_type = 'comic'
        except Comic.DoesNotExist:
            messages.error(request, 'Sorry, product you are looking \
                for is no longer available.')

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    messages.success(request, f'Successfully added {product.title} to the basket!')
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    try:
        product = Book.objects.get(pk=item_id)
        product_type = 'book'
    except Book.DoesNotExist:
        try:
            product = Comic.objects.get(pk=item_id)
            product_type = 'comic'
        except Comic.DoesNotExist:
            messages.error(request, 'Sorry, product you are looking \
                for is no longer available.')

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Successfully updated quantity of {product.title} to {quantity}!'
        )
    else:
        messages.success(request, f'Successfully removed {product.title} from the basket!')
        bag.pop(item_id)

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))


@require_POST
def remove_from_bag(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        product = Book.objects.get(pk=item_id)
        product_type = 'book'
    except Book.DoesNotExist:
        try:
            product = Comic.objects.get(pk=item_id)
            product_type = 'comic'
        except Comic.DoesNotExist:
            messages.error(request, 'Sorry, product you are looking \
                for is no longer available.')

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        request.session['bag'] = bag
        messages.success(request, f'Successfully removed {product.title} from the basket!')
        return HttpResponse(status=200)

    except KeyError:
        return JsonResponse({'error': 'Item not found in the bag'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
