from django.shortcuts import redirect
from functools import wraps

def subscription_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.subscription.is_active:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('payment_page_url') 
        
    return _wrapped_view