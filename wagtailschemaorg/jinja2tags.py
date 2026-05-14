from jinja2 import pass_context
from jinja2.ext import Extension
from wagtail.models import Site

from wagtailschemaorg import templates


@pass_context
def ld_for_site(context, site=None):
    request = context["request"]
    if site is None:
        site = Site.find_for_request(request)
    return templates.ld_for_site(site, request)


@pass_context
def ld_for_object(context, obj=None):
    if obj is None:
        obj = context["page"]
    return templates.ld_for_object(obj, context["request"])


@pass_context
def ld_print_entity(context, entity):
    return templates.ld_print_entity(entity, context["request"])


class WagtailSchemaOrgExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)

        self.environment.globals["ld"] = {
            "for_site": ld_for_site,
            "for_object": ld_for_object,
            "print_entity": ld_print_entity,
        }
