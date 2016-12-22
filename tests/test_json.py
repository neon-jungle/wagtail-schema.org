import datetime
import json
import os

from django.test import TestCase
from wagtail.wagtailcore.models import Site
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.tests.utils import get_test_image_file

from tests.app.models import PersonPage
from wagtailschemaorg.encoder import JSONLDEncoder


class TestJsonEncoding(TestCase):
    def setUp(self):
        super().setUp()
        self.image = Image.objects.create(title='Test image', file=get_test_image_file())

    def json(self, data):
        return json.dumps(data, sort_keys=True, cls=JSONLDEncoder)

    def test_image_ld(self):
        filename, _ = os.path.splitext(os.path.basename(self.image.file.name))
        url = '/media/original_images/{}.png'.format(filename)
        self.assertEqual(
            self.json({'image': self.image}),
            self.json({'image': {
                '@context': 'http://schema.org',
                '@type': 'ImageObject',
                '@id': url,
                'name': 'Test image',
                'url': url,
                'contentUrl': url,
                'contentSize': str(self.image.file.size),
                'width': {'@type': 'Distance', '@value': '640 px'},
                'height': {'@type': 'Distance', '@value': '480 px'},
                'thumbnail': '/media/images/{}.max-200x200.png'.format(filename),
            }}))

    def test_nested_object(self):
        root_page = Site.objects.get().root_page
        person = root_page.add_child(instance=PersonPage(
            title='Alex Citizen',
            bio='Alex did some things',
            date_of_birth=datetime.date(1970, 1, 1),
            photo=self.image,
        ))
        self.assertEqual(
            self.json({'person': person}),
            self.json({'person': {
                '@type': '@id',
                '@id': 'http://localhost/alex-citizen/'
            }}))
