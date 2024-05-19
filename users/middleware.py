from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse

class SubscriptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            # Check if the user has an active subscription
            subscription_end_date = request.user.profile.subscription_end_date
            if subscription_end_date and subscription_end_date < timezone.now():
                # Subscription has expired, redirect to purchase new plan
                if not request.path.startswith(reverse('subscribe')):
                    return redirect(reverse('subscribe'))

        return response