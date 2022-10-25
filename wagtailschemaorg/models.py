from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (4, 0):
    from wagtail.contrib.settings.models import BaseSiteSetting
else:
    from wagtail.contrib.settings.models import BaseSetting as BaseSiteSetting

from .jsonld import ThingLD
from .registry import SiteThingLD
from .utils import extend


class PageLDMixin(ThingLD):
    """
    Extends JSON-LD data with this page's title, url, and search_description.
    """
    def ld_get_url(self):
        return self.full_url

    def ld_entity(self):
        return extend(super(PageLDMixin, self).ld_entity(), {
            'name': self.title,
            'description': self.search_description,
        })


class BaseLDSetting(SiteThingLD, BaseSiteSetting):
    """
    A mix of :class:`~wagtailschemaorg.registry.SiteThingLD` and
    :class:`wagtail.contrib.settings.models.BaseSiteSetting`.
    """
    class Meta:
        abstract = True

    def ld_get_url(self):
        """
        The URL this object represents.
        By default it represents the whole site.
        """
        return self.site.root_url

    @classmethod
    def ld_get_for_site(cls, site):
        return cls.objects.filter(site=site).first()
