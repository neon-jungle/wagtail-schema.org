from wagtail.contrib.settings.models import BaseSiteSetting

from .jsonld import ThingLD
from .registry import SiteThingLD


class PageLDMixin(ThingLD):
    """
    Extends JSON-LD data with this page's title, url, and search_description.
    """
    def ld_get_url(self):
        return self.full_url

    def ld_entity(self):
        return {
            **super(PageLDMixin, self).ld_entity(),
            **{
                'name': self.title,
                'description': self.search_description,
            }
        }


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
