from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from myshop.models import Category, Item


def main(request):
    return HttpResponseRedirect(reverse("catalog:index"))


def index(request):
    
    if "filter" in request.GET:
        filter = request.GET["filter"]
        print(filter) # custom filter feature TODO
    if "sort" in request.GET:
        sort = request.GET["sort"]
        print(sort) # custom sort feature TODO

    return render(request, "catalog/index.html", {
        "items": Item.objects.all(),
    })


def item(request, item_id):
    try:
        item = Item.objects.get(id = item_id)
    except Item.DoesNotExist:
        return Http404("Invalid item id!")
    return render(request, "catalog/item.html", {
        "item": item,
    })
