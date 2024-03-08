from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.context import bag_content
import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products'))

    current_bag = bag_content(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OdGE0Hah1Wg4I85bA8Ge6ZT1VXnSe26INaq4kTBivI3BC577MgY9TnVvoUAr6oIby0sy0yCvkrl10ve8p5BDhjs002t8tITbL',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
