class ThingLD(object):
    def ld_get_id(self, request):
        """
        Get the id for this object. Conventionally, this is an IRI.
        Defaults to its URL.
        """
        return self.ld_get_url(request)

    def ld_get_url(self, request):
        """Get the URL for this object."""
        raise NotImplementedError

    def ld_entity(self, request):
        """Make a complete JSON-LD representation for this object."""
        return {
            '@context': 'http://schema.org',
            '@type': 'Thing',
            '@id': self.ld_get_id(request),
            'url': self.ld_get_url(request),
        }

    def ld_nested_entity(self, request):
        """
        Make a JSON-LD representation suitable for including in other entities.
        """
        return {'@type': '@id', '@id': self.ld_get_id(request)}

    def ld_entity_list(self, request):
        """A list of all the entities this object represents"""
        return [self.ld_entity(request)]
