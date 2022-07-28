from django.http import Http404
from django.db.models import Q
from django.core.exceptions import FieldError
from django.shortcuts import render
from datetime import datetime as dt, timedelta as td

from myshop.models import Item
from . import util


def main(request):
    return render(request, "catalog/main.html")


def index(request):
    items = ""

    # category filter feature
    # ex: ?category=EL_HI means filter items that has those 2 category codes
    if "category" in request.GET:
        items = Item.get_with_category_codes(request.GET["category"].split('_'))
    
    # price filter feature
    # ex: ?price=10-30 means filter all items with price between 10 until 30 dollars
    if "price" in request.GET:
        range = request.GET["price"].split('-')
        items = (Item.objects.filter(Q(price__gte=range[0]) & Q(price__lte=range[1]))
                 if items == "" else
                 items.filter(Q(price__gte=range[0]) & Q(price__lte=range[1])))
    
    # time filter feature
    # ex: ?time=3 means filter only shopping queries on the last 3 days
    if "time" in request.GET:
        try: last_n_days = float(request.GET["time"])
        except ValueError: last_n_days = 7
        items = (Item.objects.filter(time__gte = dt.now() - td(last_n_days))
                 if items == "" else
                 items.filter(time__gte = dt.now() - td(last_n_days)))
    
    # search feature
    # ex: ?search=table+wood search for all titles containing substring table or wood
    if "search" in request.GET:
        items = util.search(request) if items == "" else util.search(request, items)
    
    # sort feature (price/time/title), either ascending or descending (asc/des)
    # ex: ?sort=desprice means sort price in descending order
    if "sort" in request.GET:
        try: items = (Item.sort(request.GET["sort"]) if items == "" else
                      Item.sort(request.GET["sort"], items))
        except FieldError: pass
    
    # pagination feature
    # ex: ?num=5&page=1 means paginate 5 per page, open page 1
    return render(request, "catalog/index.html", {
        "pagination": util.paginate(
            request, (util.getcount(items) if items != "" else
                      util.getcount(Item.objects.all()))
        ),
    })


def item(request, item_id):
    # ensure that the item id is valid
    try:
        item = Item.objects.get(id = item_id)
    except Item.DoesNotExist:
        return Http404("Invalid item id!")
    
    # render page and pass these info: item query, status.creator, status.sold
    return render(request, "catalog/item.html", {
        "item": item,
        "status": item.getstatus(request.user),
        "notloggedin": request.user.is_anonymous
    })
