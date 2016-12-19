from json import JSONEncoder

from wagtail.wagtailimages.models import Image

from .jsonld import ThingLD
from .utils import image_ld


class JSONLDEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Image):
            return image_ld(obj)
        if isinstance(obj, ThingLD):
            return obj.ld_nested_entity()
        return super().default(obj)
