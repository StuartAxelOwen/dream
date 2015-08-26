""" ...dream """
__author__ = 'stuartaxelowen'

from dask import bag
from dask.async import get_sync
import toolz
import itertools
import multiprocessing


NUM_CORES = multiprocessing.cpu_count()

dreams = ('dream-%d' % i for i in itertools.count(1))


class Empty(object): pass  # Careful - `Empty` is truthy


def dfs_first_empty_path(dsk):
    """ Returns a list of dict keys leading to the first nothing """
    # TODO: Consider changing this to "find deepest Nothing"?
    for k, v in dsk.items():
        if isinstance(v, dict):
            result = dfs_first_empty_path(v)
            if isinstance(result, list):
                return [k] + result
        elif v is Empty:
            return [k]
    return None


class Dream(bag.Bag):
    """ A tool for composing dasks. """
    def __init__(self, dsk=None, name=None, npartitions=None):
        name = name or next(dreams)
        partitions = npartitions or NUM_CORES
        dsk = dsk or {(name, i): Empty for i in range(partitions)}
        for i in range(NUM_CORES):
            if (name, i) not in dsk:
                dsk[(name, i)] = tuple()
        super(Dream, self).__init__(dsk, name, partitions)

    def __call__(self, thing, *things, multiprocessing=False):
        if not self.has_empties:
            raise Exception("Can't call dream that already has a source")
        result = self
        for _thing in (thing, ) + things:
            result = result.of(_thing)
        return result.compute(multiprocessing=multiprocessing)

    def of(self, iterable):
        if self.dask.get(self.name, Empty) is not Empty:
            raise Exception("Can't call of on dream that already has a source")

        if not isinstance(iterable, bag.Bag):
            iterable = Dream(*bag.from_sequence(iterable, npartitions=NUM_CORES)._args)

        try:
            if set(self.dask.values()) == {Empty}:
                # Case for empty dreams - don't want to add unnecessary layers
                return iterable
        except TypeError: # Unhashable type -> not empty
            pass

        return _merge_dreams(iterable, self)

    def of_files(self, filenames, chunkbytes=None):
        return Dream(*bag.from_filenames(filenames, chunkbytes)._args)

    def into(self, fn):
        if self.has_empties:
            return TerminatedDream(self, fn)# TODO: how do I make this partial
        return _merge_dreams(self, fn) if isinstance(fn, Dream) else fn(self)

    def count(self, multiprocessing=False):
        return super(Dream, self).count().compute(multiprocessing=multiprocessing)

    def join(self, other=None, on=None, on_other=None):
        other = other or Dream()
        if not callable(on):
            raise ValueError("Must specify a callable `on` parameter for join")
        return super(Dream, self).join(other, on, on_other)

    def compute(self, multiprocessing=False, **kwargs):
        if multiprocessing:
            return super(Dream, self).compute(**kwargs)
        return super(Dream, self).compute(get=get_sync, **kwargs)

    @property
    def has_empties(self):
        return dfs_first_empty_path(self.dask) is not None


class TerminatedDream(object):
    def __init__(self, dream, fn):
        self.dream = dream
        self.terminator = fn

    def __call__(self, thing, *things):
        return self.terminator(self.dream(thing, *things))

    def of(self, thing):
        return self.dream.of(thing).into(self.terminator)


def _merge_dreams(first, second):
    new_dask = second.dask
    for i in range(second.npartitions):
        # Populate root of first dask into empty of second
        empty_path = dfs_first_empty_path(new_dask)
        new_dask = toolz.update_in(new_dask, empty_path,
                                   lambda _: (first.name, i))
    new_dask = toolz.merge(new_dask, first.dask)
    return type(second)(new_dask, second.name, second.npartitions)
