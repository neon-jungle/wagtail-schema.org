import jinja2
from jinja2.ext import Extension

from wagtailschemaorg import templates


@jinja2.contextfunction
def ld_for_site(context, site=None):
    if site is None:
        site = context['request'].site
    return templates.ld_for_site(site)


@jinja2.contextfunction
def ld_for_object(context, obj=None):
    if obj is None:
        obj = context['page']
    return templates.ld_for_object(obj)


def ld_print_entity(entity):
    return templates.ld_print_entity(entity)


class WagtailSchemaOrgExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)

        self.environment.globals['ld'] = {
            'for_site': ld_for_site,
            'for_object': ld_for_object,
            'print_entity': ld_print_entity,
        }
