"""
Implementation of Storms's tuple data model
"""


class Fields(object):
    def __init__(self, fields):
        self._fields = fields
        self._index = {}
        self.index()

    def index(self):
        for idx, f in enumerate(self._fields):
            self._index[f] = idx

    def field_index(self, field):
        ret = self._index.get(field)
        if not ret:
            raise ValueError('%s does not exist' % (field, ))
        return ret

    @property
    def size(self):
        return len(self._fields)

    def __contains__(self, item):
        return item in self._index

    def __getitem__(self, item):
        return self._index[item]

    def __str__(self):
        return str(self._fields)


class MessageId(object):
    def __init__(self, **other):
        if other:
            self._anchors_to_ids = other
        else:
            self._anchors_to_ids = {}

    @staticmethod
    def generate_id(rand):
        return rand.randint(_int=long)

    @staticmethod
    def make_id(other):
        return MessageId(**other)

    @staticmethod
    def make_root_id(id, val):
        return MessageId(**{id: val})

    def __hash__(self):
        return hash(self._anchors_to_ids)

    def __eq__(self, other):
        return isinstance(other, MessageId) and\
            self._anchors_to_ids == other._anchors_to_ids

    def serialize(self):
        raise NotImplementedError()

    @staticmethod
    def deserialize(msg):
        raise NotImplementedError()


class Values(tuple):
    """A convenience class for making tuple values using new Values("field1", 2, 3)

    >>> Values("field1", 2, 3)
    ("field1", 2, 3)
    """
    def __new__(cls, *args):
        return tuple(args)


if __name__ == '__main__':
    import doctest
    doctest.DocTestSuite()
