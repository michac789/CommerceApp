from django.http import JsonResponse


def api_view(*args):
    valid_methods = list(map(lambda _: _.upper(), args))
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.method in valid_methods:
                return func(request, *args, **kwargs)
            return JsonResponse({
                "error": "Invalid request method!",
            }, status = 405)
        return wrapper
    return decorator
