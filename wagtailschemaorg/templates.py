import json
from django.utils.html import format_html, _json_script_escapes
from django.utils.safestring import mark_safe

from .encoder import JSONLDEncoder
from .registry import registry


def nl(xs):
    return mark_safe('\n'.join(xs))


def ld_for_site(site, request):
    return nl([
        ld_print_entity(entity, request) for entity in registry.get_entities(site, request)
    ])


def ld_for_object(obj, request):
    return nl([
        ld_print_entity(entity, request) for entity in obj.ld_entity_list(request)
    ])


def ld_print_entity(entity, request):
    json_out = json.dumps(entity, cls=JSONLDEncoder.with_request(request), sort_keys=True).translate(_json_script_escapes)
    return format_html('<script type="application/ld+json">{}</script>', mark_safe(json_out))
