from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta
import pytz
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework import status
from payment.models import StripeWebHook, Subscription
from users.models import User


import stripe
import json

stripe.api_key = getattr(settings, 'STRIPE_SECRET_KEY', '')

@csrf_exempt
def stripe_webhook(request, selfsecret):
    staticsecret = 'xldwel54ld7&8dewlekjrweklzcxlkflsfsdxl'
    if staticsecret != selfsecret:
        raise ValueError('key is not matched, to find the right key, please check static secret, to main security, change the key after every few days')
    payload = request.body
    event = None


    event = stripe.Event.construct_from(
        json.loads(payload), stripe.api_key
    )
 

  # Handle the event
    # if event.type == 'checkout.session.completed':
    checkout_info = event.data.object
    
    client_reference_id = checkout_info.get('client_reference_id', '')
    subscription_id = checkout_info.get('subscription', '')

    customer_details = checkout_info.get('customer_details', {})
    customer_id = checkout_info.get('customer', '')
        # raise ValueError('checkout.session.completed: not this even')
        

    if client_reference_id:
        ruser = User.objects.get(usersecret=client_reference_id)
        StripeWebHook.objects.create(owner=ruser, checkout_response=checkout_info)
        subscription = Subscription.objects.get(owner=ruser)
        subscription.stripe_subscription_id = subscription_id


        retrieve_subscription = stripe.Subscription.retrieve(
            subscription_id,
        )
        if retrieve_subscription['status'] != 'active':
            subscription.is_active = False
            subscription.save()
        else:
            subscription.is_active = True
            subscription.current_period_end = datetime.fromtimestamp(retrieve_subscription.current_period_end, pytz.UTC)
            subscription.current_period_start = datetime.fromtimestamp(retrieve_subscription.current_period_start, pytz.UTC)
            subscription.save()
    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)