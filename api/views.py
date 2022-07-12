from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from commerceapp.settings import LOGIN_URL

from cart.models import Bookmark, Cart
from myshop.models import Item
from sso.models import User


def test(_):
    return JsonResponse({ "message": "API connected!", })


@csrf_exempt
@login_required(login_url=LOGIN_URL)
def bookmark(request, item_id):
    
    # 'GET': retrieve all bookmarked items
    if request.method == "GET":
        bookmarks = Bookmark.objects.filter(user = request.user)
        return JsonResponse([bm.serialize() for bm in bookmarks], safe = False)
    
    # make sure item_id is valid for 'PUT' and 'DELETE' method
    if not Item.objects.filter(id = item_id).exists():
        return JsonResponse({ "error": "Invalid item ID!" })
    
    # 'PUT': create new bookmark item if not yet created
    elif request.method == "PUT":
        Bookmark.objects.get_or_create(
            user = request.user, item = Item.objects.get(id = item_id),
        )
        return JsonResponse({ "message": "added bookmark" })
    
    # 'DELETE' delete bookmark item if exist
    elif request.method == "DELETE":
        try: Bookmark.objects.get(
                user = request.user, item = Item.objects.get(id = item_id),
            ).delete()
        except Bookmark.DoesNotExist: pass
        return JsonResponse({ "message": "removed bookmark" })
    
    # return error for other request methods
    else: return JsonResponse({ "error": "Invalid request method!"} )


@csrf_exempt
@login_required(login_url=LOGIN_URL)
def addcart(request, item_id):
    
    # 'GET': retrieve all items on cart
    if request.method == "GET":
        cart_items = Cart.objects.filter(user = request.user)
        return JsonResponse([cart.serialize() for cart in cart_items], safe = False)
    
    # make sure item_id is valid for 'PUT' and 'DELETE' method
    if not Item.objects.filter(id = item_id).exists():
        return JsonResponse({ "error": "Invalid item ID!" })
    
    # 'PUT': create new cart item if not yet created
    elif request.method == "PUT":
        try: Cart.objects.get_or_create(
            user = request.user, item = Item.objects.get(id = item_id),
        )
        # you cannot add your own item on sale or add closed item
        except Exception as e:
            return JsonResponse({ "error": e.args[0] })
        return JsonResponse({ "message": "added to cart" })
    
    # 'DELETE' delete bookmark item if exist
    elif request.method == "DELETE":
        try: Cart.objects.get(
                user = request.user, item = Item.objects.get(id = item_id),
            ).delete()
        except Cart.DoesNotExist: pass
        return JsonResponse({ "message": "removed from cart" })
    
    # return error for other request methods
    else: return JsonResponse({ "error": "Invalid request method!"} )
