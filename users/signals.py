from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model

from payment.models import Subscription
from users.models import Profile


User = get_user_model()



@receiver(post_save, sender=User)
def create_subscription(sender, instance, created, **kwargs):
    if created:
        Subscription.objects.create(owner=instance)
        Profile.objects.create(user=instance)

