from .jsonld import ThingLD


class Registry(object):
    def __init__(self):
        self.items = []

    def register(self, getter):
        self.items.append(getter)

    def get_entities(self, site):
        for getter in self.items:
            obj = getter(site)
            if obj is None:
                continue
            yield from obj.ld_entity_list()


class SiteThingLD(ThingLD):
    """A SiteThingLD can get a ThingLD instance for a wagtailcore.Site"""
    def ld_get_for_site(self, site):
        """
        Given a wagtailcore.Site, return a ThingLD instance.
        Returns None if there is no relevant instance for this site.
        """
        raise NotImplementedError()


registry = Registry()


def register_site_thing(site_thing):
    """
    Register a SiteThingLD class to be included in ``{% ld_for_site %}``.
    """
    register_site_func(site_thing.ld_get_for_site)
    return site_thing


def register_site_func(func):
    registry.register(func)
    return func
