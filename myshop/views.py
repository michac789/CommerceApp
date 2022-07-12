from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .decorators import seller_required
from .forms import ItemForm, SellerRegistrationForm
from .models import Item, Seller


def main(request):
    # when user is not logged in yet (show different html view)
    if request.user.is_anonymous:
        return render(request, "myshop/main.html", {
            "notloggedin": True,
        })
    
    # when there is query parameter, use different model manager
    if "status" in request.GET:
        if request.GET["status"] == "sold":
            items = Item.sold.filter(seller=request.user)
        elif request.GET["status"] == "onsale":
            items = Item.onsale.filter(seller=request.user)
        else: items = Item.objects.filter(seller=request.user)
    else: items = Item.objects.filter(seller=request.user)
    
    # user is logged in, query all their items on sale
    return render(request, "myshop/main.html", {
        "items": items,
        "notloggedin": False,
        "notseller": not hasattr(request.user, 'seller'),
    })


@login_required(login_url="sso:login")
def register(request):
    # 'post' method: register new seller from existing user
    if request.method == "POST":
        form = SellerRegistrationForm(request.POST)
        if form.is_valid():
            Seller.objects.create(
                user = request.user,
                location = form.cleaned_data["location"],
            )
            return HttpResponseRedirect(reverse("myshop:main"))
        else: return render(request, "myshop/register.html", {
                "form": form,
            })
    
    # 'get' method: load empty form
    else: return render(request, "myshop/register.html", {
            "form": SellerRegistrationForm(),
        })


@login_required(login_url="sso:login")
@seller_required
def create(request):
    # 'post' method: create new item and save to database
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
        
        # if form is invalid, do not update database
        else: return render(request, "myshop/create.html", {
            "form": form,
        })
    
    # 'get' method: render empty form
    else: return render(request, "myshop/create.html", {
        "form": ItemForm(),
    })


@login_required(login_url="sso:login")
@seller_required
def edit(request, item_id):
    # ensure that the item id is valid
    try:
        item = Item.objects.get(id = item_id)
    except Item.DoesNotExist:
        return Http404("Invalid item id!")
    
    # ensure that the user is indeed the seller to allow edit
    if request.user != item.seller:
        return HttpResponse("Unauthorized user!", status = 401)
    
    # 'post' method: update changes to database
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item.title = form.cleaned_data["title"]
            item.description = form.cleaned_data["description"]
            item.image = form.cleaned_data["image"]
            item.price = form.cleaned_data["price"]
            item.category = form.cleaned_data["category"]
            item.save()
            return HttpResponseRedirect(reverse("catalog:item", args=(
                item.id,
            )))
        
        # if form is invalid, do not update database
        else: return render(request, "myshop/create.html", {
            "form": form,
        })
    
    # 'get' method: render form and prepopulate with existing value
    return render(request, "myshop/edit.html", {
        "form": ItemForm(item.formhandler())
    })
