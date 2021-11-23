from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from shopping_cart.models import Cart


@receiver(post_save, sender=get_user_model())
def creat_shopping_cart(sender, instance, **kwargs):
    if not Cart.objects.filter(user_id=instance.id).first():
        Cart.objects.create(user_id=instance.id)
