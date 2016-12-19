from django.test import SimpleTestCase

from wagtailschemaorg.templates import ld_print_entity


class TestPrintEntity(SimpleTestCase):
    def test_simple_object(self):
        out = ld_print_entity({'@type': 'Misc', 'hello': 'world'})
        self.assertEqual(
            out,
            '<script type="application/ld+json">{"@type": "Misc", "hello": "world"}</script>')
