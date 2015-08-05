''' ...dream '''
__author__ = 'stuartaxelowen'

from dask import bag
import toolz
import itertools
import sys

dreams = ('dream-%d' % i for i in itertools.count(1))


class Nothing(object): pass  # Careful - `Nothing` is truthy


def dfs_first_nothing_path(dsk):
    ''' Returns a list of dict keys leading to the first nothing '''
    # TODO: Consider changing this to "find deepest Nothing"?
    for k, v in dsk.items():
        if isinstance(v, dict):
            result = dfs_first_nothing_path(v)
            if isinstance(result, list):
                return [k] + result
        elif v is Nothing:
            return [k]
    return None


class Dream(bag.Bag):
    def __init__(self, dsk=None, name=None, npartitions=1):
        name = name or next(dreams)
        super(Dream, self).__init__(dsk or {(name, 0): Nothing}, name, npartitions)

    def __call__(self, thing):
        if self.dask.get(self.name, Nothing) is not Nothing:
            raise Exception("Can't call dream that already has a source")
        return self.of(thing)

    def of(self, iterable, *iterables):
        pprint(self.dask)
        if self.dask.get(self.name, Nothing) is not Nothing:
            raise Exception("Can't call of on dream that already has a source")

        new_dask = self.dask
        for _iterable in (iterable,) + iterables:
            input_path = dfs_first_nothing_path(self.dask)
            new_dask = toolz.update_in(self.dask, input_path, lambda _: tuple(_iterable))
            print(self.name)

        # TODO make it partition properly
        return type(self)(new_dask, self.name, npartitions=self.npartitions)

    def of_files(self, filenames, chunkbytes=None):
        return self.of(bag.from_filenames(filenames, chunkbytes))

    def into(self, fn):
        if isinstance(fn, Dream):
            new_dask = toolz.merge(self.dask, fn.dask)
            input_path = dfs_first_nothing_path(fn.dask)
            new_dask = toolz.update_in(new_dask, input_path, lambda _: (self.name, 0))
            return type(self)(new_dask, fn.name, npartitions=self.npartitions)
        return fn(self)
