from django.template import Library
from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.models import Site
else:
    from wagtail.core.models import Site

from wagtailschemaorg import templates

register = Library()


@register.simple_tag(takes_context=True)
def ld_for_site(context, site=None):
    if site is None:
        site = Site.find_for_request(context["request"])
    return templates.ld_for_site(site)


@register.simple_tag(takes_context=True)
def ld_for_object(context, obj=None):
    if obj is None:
        obj = context["page"]
    return templates.ld_for_object(obj)


@register.simple_tag
def ld_print_entity(entity):
    return templates.ld_print_entity(entity)
