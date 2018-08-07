from json import JSONEncoder

from .jsonld import ThingLD
from .utils import image_ld

try:
    from wagtail.images.models import Image
except ImportError:  # fallback for Wagtail <2.0
    from wagtail.wagtailimages.models import Image


class JSONLDEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Image):
            return image_ld(obj)
        if isinstance(obj, ThingLD):
            return obj.ld_nested_entity()
        return super(JSONLDEncoder, self).default(obj)
