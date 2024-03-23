from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about_us, name='about_us'),
    path('policy/', views.privacy_policy, name='privacy_policy'),
]
