from json import JSONEncoder

from wagtail.images.models import Image

from .jsonld import ThingLD
from .utils import image_ld


class JSONLDEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Image):
            return image_ld(obj, self.request)
        if isinstance(obj, ThingLD):
            return obj.ld_nested_entity(self.request)
        return super().default(obj)

    @staticmethod
    def with_request(request):
        return type("JSONLDRequestEncoder", (JSONLDEncoder,), {"request": request})
