from functools import partial
from urllib.parse import urljoin


def extend(*ds):
    """
    Shortcut for updating a dict in a single line. Useful when updating a
    dict from a super class:

    .. code-block:: python

        class Parent(object):
            def get_json(self):
                return {
                    'foo': 1,
                    'bar': 2,
                }

        class Child(Parent):
            def get_json(self):
                return extend(super().get_json(), {
                    'bar': 3,
                    'quux': 4,
                })
    """
    out = {}
    for d in ds:
        out.update(d)
    return out


def simple_type(type, value):
    return {'@type': type, '@value': value}


Distance = partial(simple_type, 'Distance')


def image_ld(image, thumbnail_filter="max-200x200", base_url=None):
    # Support custom image models with a to_json_ld() method
    if hasattr(image, 'to_json_ld'):
        return image.ld_entity()

    thumbnail = image.get_rendition(thumbnail_filter)

    return {
        '@context': 'http://schema.org',
        '@type': 'ImageObject',
        '@id': urljoin(base_url, image.file.url),
        'name': image.title,
        'url': urljoin(base_url, image.file.url),
        'contentUrl': urljoin(base_url, image.file.url),
        'contentSize': str(image.file.size),
        'width': Distance('{} px'.format(image.width)),
        'height': Distance('{} px'.format(image.height)),
        'thumbnail': urljoin(base_url, thumbnail.url),
    }
