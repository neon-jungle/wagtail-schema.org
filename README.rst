==================
wagtail-schema.org
==================

Add Schema.org JSON-LD to your website

Installing
==========

wagtail-schema.org supports Wagtail 2.0 upwards.

Install using pip:

.. code-block:: console

    $ pip install wagtail-schema.org

Add it to your ``INSTALLED_APPS`` to use the Django template tags:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'wagtailschemaorg',
    ]

Using
=====

``wagtail-schema.org`` supports two types of schema entities:
site-wide entities and page-specific entities.
Site-wide entities might be the organisation that the site as a whole is about,
while page-specific entities might be a single person that the page in question is about.
Both sets of entities are optional, and
sites can implement only those that make sense.

Site-wide entities
------------------

A site-wide entity is printed on every page
using the ``{% ld_for_site %}`` template tag.
They should be entities that are relevant to the whole site,
such as the Organisation or Person that the site is about.
Multiple (or zero) site-wide entities can exist for a site.

.. code-block:: python

    from django.db import models
    from wagtail.contrib.settings.models import register_setting

    from wagtailschemaorg.models import BaseLDSetting
    from wagtailschemaorg.registry import register_site_thing
    from wagtailschemaorg.utils import extend


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
                '@type': 'Organization',
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

.. note:: Every site-wide Thing should have a different ``@id``.
    By default, the ``@id`` is the Thing's ``url``.
    You can change a Thing's ``@id`` by overriding
    ``ld_get_id`` or ``ld_get_url`` as required.

Page-specific entities
----------------------

Each page can specify a list of relevant entities.
Use ``{% ld_for_object page %}`` to print these.

.. code-block:: python

    from django.db import models
    from wagtail.admin.edit_handlers import FieldPanel
    from wagtail.core.models import Page
    from wagtail.images.edit_handlers import ImageChooserPanel

    from testapp.models import TestOrganisation
    from wagtailschemaorg.models import PageLDMixin
    from wagtailschemaorg.utils import extend, image_ld


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

In templates
============

``wagtail-schema.org`` provides two template tags:
one for printing out the site-wide entities and
one for page-specific entities.

Django templates
----------------

Make sure that ``wagtailschemaorg`` is in your ``INSTALLED_APPS``,
and add ``{% load wagtailschemaorg_tags %}`` to the top of your template.

``{% ld_for_site [site] %}``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Print all the site-wide entities for a site.
Takes an optional ``site`` argument,
which defaults to the site from the current template request context.
See ``register_site_thing`` for more information on site-wide entities.

``{% ld_for_object [obj] %}``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Print all the entities for ``obj``.
``obj`` is optional, and defaults to ``page`` in the current template context.
``obj`` should implement the ``ThingLD`` interface.
Calls ``obj.ld_to_data_list``, and prints all the entities returned.

``{% ld_print_entity entity %}``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Print an entity directly. ``entity`` should be a ``dict`` with JSON-LD data.

Jinja2 templates
~~~~~~~~~~~~~~~~

Add ``wagtailschemaorg.jinja2tags.WagtailSchemaOrgExtension`` to your Jinja2 extensions.

``{{ ld.for_site([site]) %}``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Print all the site-wide entities for a site.
Takes an optional ``site`` argument,
which defaults to the site from the current template request context.
See ``register_site_thing`` for more information on site-wide entities.

``{% ld.for_object([obj]) %}``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Print all the entities for ``obj``.
``obj`` is optional, and defaults to ``page`` in the current template context.
``obj`` should implement the ``ThingLD`` interface.
Calls ``obj.ld_to_data_list``, and prints all the entities returned.

``{% ld.print_entity(entity) %}``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Print an entity directly. ``entity`` should be a ``dict`` with JSON-LD data.
