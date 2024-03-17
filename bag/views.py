from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages


def view_bag(request):
    """ A view to renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    messages.success(request, 'Successfully added product to the basket!')
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, 'Successfully updated quantity of the product!'
        )
    else:
        messages.success(request, 'Successfully removed product from the basket!')
        bag.pop(item_id)

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))


@require_POST
def remove_from_bag(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        request.session['bag'] = bag
        messages.success(request, 'Successfully removed product from the basket!')
        return HttpResponse(status=200)

    except KeyError:
        return JsonResponse({'error': 'Item not found in the bag'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
