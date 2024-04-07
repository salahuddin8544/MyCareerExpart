from django.urls import path
from payment import views

urlpatterns = [
    path('stripe_webhook/<str:selfsecret>/', views.stripe_webhook, name='stripe_webhook'),
]
