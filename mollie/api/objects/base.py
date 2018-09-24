class Base(dict):

    _resource = None

    def __init__(self, data, resource=None, client=None):
        """
        Create a new object from API result data.

        We optionally initialize the _resource variable to be able to use this when querying the API
        for additional data defined as an endpoint in the _links attribute.

        TODO: remove self._resource when all of its usage is refactored to using self.client
        """
        super(Base, self).__init__(data)
        self._resource = resource
        self.client = client

    def _get_property(self, name):
        """Return the named property from dictionary values."""
        if name not in self:
            return None
        return self[name]

    def _get_link(self, name):
        """Return a link by its name."""
        try:
            return self['_links'][name]['href']
        except (KeyError, TypeError):
            return None

    @classmethod
    def get_object_name(cls):
        return '{name}s'.format(name=cls.__name__.lower())

    @classmethod
    def get_resource_class(cls, client):
        raise NotImplementedError
