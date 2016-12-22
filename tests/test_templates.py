import datetime
import json

from django.template import engines
from django.test import RequestFactory, TestCase
from wagtail.wagtailcore.models import Site
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.tests.utils import get_test_image_file

from tests.app.models import PersonPage, TestOrganisation
from wagtailschemaorg import templates
from wagtailschemaorg.utils import image_ld


class BaseTestCase(TestCase):
    def setUp(self):
        super().setUp()

        self.site = Site.objects.get()
        self.organisation = TestOrganisation.objects.create(
            site=self.site,
            name='Test organisation',
            phone_number='555-1234',
            email='org@example.com',
            twitter_handle='org',
            facebook_url='http://facebook.com/org',
        )

        root_page = self.site.root_page
        self.image = Image.objects.create(title='Test image', file=get_test_image_file())
        self.person = root_page.add_child(instance=PersonPage(
            title='Alex Citizen',
            bio='Alex did some things',
            date_of_birth=datetime.date(1970, 1, 1),
            photo=self.image,
        ))


class TestTemplateFunctions(BaseTestCase):

    def script(self, data):
        return '<script type="application/ld+json">{}</script>'.format(
            json.dumps(data, sort_keys=True))

    def test_for_site(self):
        out = templates.ld_for_site(self.site)
        self.assertEqual(out, self.script({
            '@context': 'http://schema.org',
            '@id': 'http://localhost',
            '@type': 'Organisation',
            'email': 'org@example.com',
            'name': 'Test organisation',
            'sameAs': ['https://twitter.com/org', 'http://facebook.com/org'],
            'telephone': '555-1234',
            'url': 'http://localhost',
        }))

    def test_for_object(self):
        out = templates.ld_for_object(self.person)
        self.assertEqual(out, self.script({
            '@context': 'http://schema.org',
            '@id': 'http://localhost/alex-citizen/',
            '@type': 'Person',
            'birthDate': '1970-01-01',
            'description': '',
            'image': image_ld(self.image, base_url='http://localhost'),  # tested separately
            'name': 'Alex Citizen',
            'organisation': {
                '@id': 'http://localhost',
                '@type': '@id',
            },
            'url': 'http://localhost/alex-citizen/',
        }))

    def test_print_entity(self):
        out = templates.ld_print_entity({'@type': 'Misc', 'hello': 'world'})
        self.assertEqual(out, self.script({
            '@type': 'Misc', 'hello': 'world',
        }))


class TemplateTestMixin(object):
    def setUp(self):
        super().setUp()

        self.factory = RequestFactory()
        self.request = self.factory.get('/test/')
        self.request.site = self.site

    def render(self, string, context=None, request_context=True):
        if context is None:
            context = {}

        # Add a request to the template, to simulate a RequestContext
        if request_context:
            context['request'] = self.request

        template = self.engine.from_string(string)
        return template.render(context)

    def test_ld_for_object_implicit(self):
        context = {'page': self.person}
        out = self.render_for_object_implicit(context)
        self.assertEqual(out, templates.ld_for_object(self.person))

    def test_ld_for_object_named(self):
        context = {'item': self.person}
        out = self.render_for_object_named(context)
        self.assertEqual(out, templates.ld_for_object(self.person))

    def test_ld_for_site_implicit(self):
        context = {}
        out = self.render_for_site_implicit(context)
        self.assertEqual(out, templates.ld_for_site(self.site))

    def test_ld_for_site_named(self):
        context = {'item': self.site}
        out = self.render_for_site_named(context, request_context=False)
        self.assertEqual(out, templates.ld_for_site(self.site))


class TestDjangoTags(TemplateTestMixin, BaseTestCase):
    engine = engines['django']

    def render_for_object_implicit(self, context, **kwargs):
        return self.render("{% load wagtailschemaorg_tags %}{% ld_for_object %}", context, **kwargs)

    def render_for_object_named(self, context, **kwargs):
        return self.render("{% load wagtailschemaorg_tags %}{% ld_for_object item %}", context, **kwargs)

    def render_for_site_implicit(self, context, **kwargs):
        return self.render("{% load wagtailschemaorg_tags %}{% ld_for_site %}", context, **kwargs)

    def render_for_site_named(self, context, **kwargs):
        return self.render("{% load wagtailschemaorg_tags %}{% ld_for_site item %}", context, **kwargs)


class TestJinja2Tags(TemplateTestMixin, BaseTestCase):
    engine = engines['jinja2']

    def render_for_object_implicit(self, context, **kwargs):
        return self.render("{{ ld.for_object() }}", context, **kwargs)

    def render_for_object_named(self, context, **kwargs):
        return self.render("{{ ld.for_object(item) }}", context, **kwargs)

    def render_for_site_implicit(self, context, **kwargs):
        return self.render("{{ ld.for_site() }}", context, **kwargs)

    def render_for_site_named(self, context, **kwargs):
        return self.render("{{ ld.for_site(item) }}", context, **kwargs)
