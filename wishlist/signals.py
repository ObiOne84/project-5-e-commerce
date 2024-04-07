from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Wishlist


@receiver(post_save, sender=User)
def create_user_wishlist(sender, instance, created, **kwargs):
    if created:
        Wishlist.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_wishlist(sender, instance, **kwargs):
    try:
        instance.wishlist.save()
    except Wishlist.DoesNotExist:
        Wishlist.objects.create(user=instance)
