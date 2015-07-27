__author__ = 'stuart'

from dask import bag
import itertools
from toolz import partition_all
import math

_map = map
_filter = filter

dreams = ('sheep-number-%d' % i for i in itertools.count(1))

def of(source):
    return Dream.of(source)

def map(fn):
    return EmptyDream.map(fn)

def filter(pred):
    return EmptyDream.filter(pred)

def to(fn):
    def toer(source):
        return Dream.of(source).to(fn)
    return toer


class Nothing(object):
    pass


class EmptyDream(object):
    @staticmethod
    def partial_of(operation):
        return PartialDream.partial_of(operation)

    @classmethod
    def map(cls, fn):
        return cls.partial_of([('map', fn)])

    @classmethod
    def filter(cls, pred):
        return cls.partial_of([('filter', pred)])


class PartialDream(object):
    @staticmethod
    def of(stream):
        return Dream.of(stream)

    @staticmethod
    def partial_of(operation):
        return PartialDream(operation)

    def __init__(self, operations):
        self.operations = operations

    def __call__(self, stream):
        _dream = self.of(stream)
        for method, fn in self.operations:
            if fn is not Nothing:
                _dream = getattr(_dream, method)(fn)
            else:
                _dream = getattr(_dream, method)()
        return _dream

    def map(self, fn):
        return self.partial_of(self.operations + [('map', fn)])

    def filter(self, fn):
        return self.partial_of(self.operations + [('filter', fn)])

    def to(self, fn):
        return self.partial_of(self.operations + [('to', fn)])

    def collect(self):
        return self.partial_of(self.operations + [('collect', Nothing)])


class Dream(bag.Bag):
    @staticmethod
    def _bag(dsk, name, npartitions):
        return Dream(dsk, name, npartitions)

    @classmethod
    def of(cls, source, partition_size=None, npartitions=None):
        source = list(source)
        if npartitions and not partition_size:
            partition_size = int(math.ceil(len(source) / npartitions))
        if npartitions is None and partition_size is None:
            if len(source) < 100:
                partition_size = 1
            else:
                partition_size = int(len(source) / 100)

        parts = list(partition_all(partition_size, source))
        name = next(dreams)
        d = dict(((name, i), part) for i, part in enumerate(parts))
        return cls._bag(d, name, len(d))

    def collect(self):
        return self.compute()

    def to(self, fn):
        return fn(self)
