from django import template
register = template.Library()


@register.filter(name="slugsort")
def slugify_sort(value):
    if len(value) == 0: return "Unsorted"
    order = "Ascending" if value[:3] == "asc" else "Descending"
    return f"{value[3:].capitalize()} {order}"
