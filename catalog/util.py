from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
