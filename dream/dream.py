""" ...dream """
__author__ = 'stuartaxelowen'

from dask import bag
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

    def __call__(self, thing):
        if self.dask.get(self.name, Empty) is not Empty:
            raise Exception("Can't call dream that already has a source")
        return self.of(thing)

    def of(self, iterable):
        if self.dask.get(self.name, Empty) is not Empty:
            raise Exception("Can't call of on dream that already has a source")

        if not isinstance(iterable, bag.Bag):
            iterable = Dream(*bag.from_sequence(iterable, npartitions=NUM_CORES)._args)

        if set(self.dask.values()) == {Empty}:
            # Case for empty dreams - don't want to
            return iterable

        return _merge_dreams(iterable, self)

    def of_files(self, filenames, chunkbytes=None):
        return Dream(*bag.from_filenames(filenames, chunkbytes)._args)

    def into(self, fn):
        return _merge_dreams(self, fn) if isinstance(fn, Dream) else fn(self)

    def count(self):
        return super(Dream, self).count().compute()


def _merge_dreams(first, second):
    new_dask = second.dask
    for i in range(second.npartitions):
        # Populate root of first dask into empty of second
        empty_path = dfs_first_empty_path(new_dask)
        new_dask = toolz.update_in(new_dask, empty_path,
                                   lambda _: (first.name, i))
    new_dask = toolz.merge(new_dask, first.dask)
    return type(second)(new_dask, second.name, second.npartitions)
