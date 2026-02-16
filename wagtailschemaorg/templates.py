import json
from django.utils.html import format_html, _json_script_escapes
from django.utils.safestring import mark_safe

from .encoder import JSONLDEncoder
from .registry import registry


def nl(xs):
    return mark_safe('\n'.join(xs))


def ld_for_site(site):
    return nl(map(ld_print_entity, registry.get_entities(site)))


def ld_for_object(obj):
    return nl(map(ld_print_entity, obj.ld_entity_list()))


def ld_print_entity(entity):
    json_out = json.dumps(entity, cls=JSONLDEncoder, sort_keys=True).translate(_json_script_escapes)
    return format_html('<script type="application/ld+json">{}</script>', mark_safe(json_out))
