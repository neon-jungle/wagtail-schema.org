from functools import partial
from urllib.parse import urljoin

def simple_type(type, value):
    return {'@type': type, '@value': value}


Distance = partial(simple_type, 'Distance')


def image_ld(image, thumbnail_filter="max-200x200", base_url=None):
    # Support custom image models with a to_json_ld() method
    if hasattr(image, 'to_json_ld'):
        return image.ld_entity()

    thumbnail = image.get_rendition(thumbnail_filter)
    url = urljoin(base_url, image.file.url)

    return {
        '@context': 'http://schema.org',
        '@type': 'ImageObject',
        '@id': url,
        'name': image.title,
        'url': url,
        'contentUrl': url,
        'contentSize': str(image.file.size),
        'width': Distance('{} px'.format(image.width)),
        'height': Distance('{} px'.format(image.height)),
        'thumbnail': urljoin(base_url, thumbnail.url),
    }
