from django.db import models

from users.admin import User

class BaseModels(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class StripeWebHook(BaseModels):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    checkout_response = models.JSONField(null=True, blank=True)

class Subscription(BaseModels):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="subscription"
    )
    stripe_subscription_id = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    current_period_end = models.DateTimeField(null=True, blank=True)
    current_period_start =  models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.owner)
    
