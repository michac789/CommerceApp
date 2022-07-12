from django.contrib.auth.decorators import user_passes_test
from commerceapp.settings import SELLER_REGISTRATION_URL


def seller_required(function=None):
    decorator = user_passes_test(
        lambda user: hasattr(user, "seller"),
        login_url = SELLER_REGISTRATION_URL,
        redirect_field_name = 'next',
    )
    return decorator(function) if function else decorator
