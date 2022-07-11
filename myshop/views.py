from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import ItemForm
from .models import Item


def main(request):
    if request.user.is_anonymous:
        return render(request, "myshop/main.html", {
            "notloggedin": True,
        })
    return render(request, "myshop/main.html", {
        "items": Item.objects.filter(seller=request.user),
        "notloggedin": False,
    })


@login_required(login_url="sso:login")
def create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            new_item = Item.objects.create(
                title = form.cleaned_data["title"],
                description = form.cleaned_data["description"],
                image = form.cleaned_data["image"],
                price = form.cleaned_data["price"],
                category = form.cleaned_data["category"],
                seller = request.user,
            )
            return HttpResponseRedirect(reverse("catalog:item", kwargs={
                "item_id": new_item.id,
            }))
            
        else: return render(request, "myshop/create.html", {
            "form": form,
        })
    
    else: return render(request, "myshop/create.html", {
        "form": ItemForm(),
    })
