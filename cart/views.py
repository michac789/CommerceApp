from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.base import TemplateView
from cart.models import Cart
from myshop.models import Item


@method_decorator(login_required, name="dispatch")
class ViewCart(TemplateView):
    template_name = "cart/index.html"


@method_decorator(login_required, name="dispatch")
class Buy(View):
    def post(self, request):
        cart_items = Cart.objects.filter(user = request.user)
        item_ids = [cart_item.item.id for cart_item in cart_items]
        error = None
        for item_id in item_ids:
            try:
                item = Item.objects.get(id = item_id)
            except Item.DoesNotExist:
                error = f"Error! Item id {item_id} does not exist!"
            if item.closed == True:
                error = f"Error! The item {item.title} (id {item_id}) has been sold out! Please remove it from your cart!"
        if len(item_ids) == 0:
            error = f"Error! No item on cart!"
        if error: return render(request, "cart/index.html", {
            "error": error,
        })
        Item.buy(item_ids, request.user)
        for item_id in item_ids:
            c = Cart.objects.filter(item = Item.objects.get(id = item_id), user = request.user)
            c.delete()
        return render(request, "cart/success.html")
