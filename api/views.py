from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# API routes - TODO
def test(request):
    return JsonResponse({
        "message": "123",
    })


@csrf_exempt
@login_required(login_url="sso:login")
def addcart(request):
    pass # TODO
