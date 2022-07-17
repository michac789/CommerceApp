from django.http import Http404
from django.db.models import Q
from django.shortcuts import render

from myshop.models import Item
from . import util


def main(request):
    return render(request, "catalog/main.html")


def index(request):
    items = ""

    # query parameter category filter
    # ex: ?category=EL_HI means filter items that has those 2 category codes
    if "category" in request.GET:
        items = Item.get_with_category_codes(request.GET["category"].split('_'))
    
    # query parameter price filter
    # ex: ?price=10-30 means filter all items with price between 10 until 30 dollars
    if "price" in request.GET:
        range = request.GET["price"].split('-')
        items = (Item.objects.filter(Q(price__gte=range[0]) & Q(price__lte=range[1]))
                 if items == "" else
                 items.filter(Q(price__gte=range[0]) & Q(price__lte=range[1])))
    
    # TODO - filter time
    if "filter" in request.GET:
        filter = request.GET["filter"].split('-')
        print(filter)
    
    # TODO - sort feature
    if "sort" in request.GET:
        sort = request.GET["sort"]
        print(sort) # custom sort feature TODO
    
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
