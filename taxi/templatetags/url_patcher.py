from django import template

register = template.Library()


@register.simple_tag
def append_get_url(request, **kwargs):
    updated = request.GET.copy()
    for key in kwargs:
        if kwargs[key] is not None:
            updated[key] = kwargs[key]

    return '?' + updated.urlencode()
