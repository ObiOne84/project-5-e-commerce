from django.shortcuts import render, reverse, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    """
    A view to return the contact page and handle 
    the contact form
    """

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
        
            email = EmailMessage(
                subject=f'New contact from {name}',
                body=(f'Name: {name}\nEmail: {email}\n'
                f'Message: {message}\n'
                'Regards'),
                to=['stepienszymon9@gmail.com']
            )
            email.send()
            messages.success(request, "Thank you, your form was submitted successfully!\
                One of our team members will be in contact with you shortly.")
            return redirect(reverse('products'))
        else:
            messages.error(request, "Sorry, there was problem with your form.")
    
    template = 'home/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def faq(request):
    """ A view to return the faq page """

    return render(request, 'home/faq.html')


def about_us(request):
    """ A view to return the faq page """

    return render(request, 'home/about_us.html')
