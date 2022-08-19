from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myshop.models import Item
from cart.models import Bookmark


# function to create dynamic pagination
def paginate(request, posts):
    num = (10 if "num" not in request.GET else request.GET["num"])
    p = Paginator(posts, num)
    if "page" in request.GET:
        try:
            output_page = p.page(request.GET["page"])
        except PageNotAnInteger:
            return p.page(1)
        except EmptyPage:
            if int(request.GET["page"]) < 1:
                output_page = p.page(1)
            else:
                output_page = p.page(p.num_pages)
        return output_page
    else: return p.page(1)


# keep track of number count during pagination
def getcount(posts, start=1):
    for (i, post) in enumerate(posts):
        newpost = post
        newpost.count = i + start
    return posts


# search all that match a particular query
def search(request, items=Item.objects.all()):
    queries = request.GET.get('search', None).split(' ')
    search_results = []
    for query in queries:
        for item in items:
            if query.upper() in item.title.upper() and item.id not in search_results:
                search_results.append(item.id)
    return Item.objects.filter(id__in = search_results)


# return a queryset that is all items bookmarked by the user
def bookmark(request, items=Item.objects.all()):
    bookmarks = Bookmark.objects.filter(user = request.user)
    items_id = [bm.item.id for bm in bookmarks]
    return items.filter(id__in=items_id)
