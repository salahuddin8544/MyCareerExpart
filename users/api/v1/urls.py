# urls.py
from django.urls import path
from users.api.v1.views import SignupView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.api.v1.views import CustomTokenObtainPairView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/signup/<uuid:referral_link>/', SignupView.as_view(), name='signup_with_referral'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), # login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
