# notarcpy

"""
(I Can't Believe It's) Not ArcPy: fake objects to make testing possible.

Give it a GeoJSON feature collection and notarcpy tries to make it into
an ArcPy feature class.
"""

__version__ = "0.1"

from collections import namedtuple

FakeField = namedtuple('FakeField', 'name type')

class FakeModule(object):
    """Holds fields (TODO: rows)"""

    def __init__(self, **kw):
        self._fields = {}

    def setField(self, featureclass, fake):
        if not featureclass in self._fields:
            self._fields[featureclass] = set()
        self._fields[featureclass].add(fake)

    def ListFields(self, featureclass):
        return list(self._fields[featureclass])

