class ThingLD(object):
    def ld_get_id(self):
        """
        Get the id for this object. Conventionally, this is an IRI.
        Defaults to its URL.
        """
        return self.ld_get_url()

    def ld_get_url(self):
        """Get the URL for this object."""
        raise NotImplementedError

    def ld_entity(self):
        """Make a complete JSON-LD representation for this object."""
        return {
            '@context': 'http://schema.org',
            '@type': 'Thing',
            '@id': self.ld_get_id(),
            'url': self.ld_get_url(),
        }

    def ld_nested_entity(self):
        """
        Make a JSON-LD representation suitable for including in other entities.
        """
        return {'@type': '@id', '@id': self.ld_get_id()}

    def ld_entity_list(self):
        """A list of all the entities this object represents"""
        return [self.ld_entity()]
