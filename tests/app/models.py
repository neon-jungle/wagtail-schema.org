from django.db import models
from wagtail.contrib.settings.models import register_setting
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from wagtailschemaorg.models import BaseLDSetting, PageLDMixin
from wagtailschemaorg.registry import register_site_thing
from wagtailschemaorg.utils import extend, image_ld


@register_setting
@register_site_thing
class TestOrganisation(BaseLDSetting):
    """Details about this organisation"""
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    twitter_handle = models.CharField(max_length=15)
    facebook_url = models.URLField()

    def ld_entity(self):
        return extend(super().ld_entity(), {
            '@type': 'Organisation',
            'name': self.name,
            'email': self.email,
            'telephone': self.phone_number,
            'sameAs': [
                self.twitter_url,
                self.facebook_url,
            ],
        })

    @property
    def twitter_url(self):
        return 'https://twitter.com/' + self.twitter_handle


class PersonPage(PageLDMixin, Page):
    bio = models.TextField()
    date_of_birth = models.DateField()
    photo = models.ForeignKey('wagtailimages.Image', on_delete=models.PROTECT)

    content_panels = Page.content_panels + [
        FieldPanel('bio'),
        FieldPanel('date_of_birth'),
        ImageChooserPanel('photo'),
    ]

    def ld_entity(self):
        site = self.get_site()
        return extend(super().ld_entity(), {
            '@type': 'Person',
            'birthDate': self.date_of_birth.isoformat(),
            'image': image_ld(self.photo, base_url=site.root_url),
            'organisation': TestOrganisation.for_site(site),
        })
