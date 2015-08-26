
# import dream.dream3 as dream
import dream
from dream.dream import Empty, dfs_first_empty_path
from collections import namedtuple
from operator import add


def test_of_basic():
    assert len(dream.of(range(3)).dask.items()) == 4


def test_map_basic():
    assert dream.of(range(7)).map(lambda n: n + 1).into(sum) == sum(map(lambda n: n + 1, range(7)))
    assert dream.of(range(3)).into(sum) == sum(range(3))


def test_filter_basic():
    assert dream.of(range(4)).filter(lambda n: n % 2 == 0).into(sum) == 2


def test_dfs_empty_search():
    dsk = {'a': Empty}
    assert dfs_first_empty_path(dsk) == ['a']
    dsk = {'a': {'b': 1}, 'c': {None: Empty}}
    assert dfs_first_empty_path(dsk) == ['c', None]
    assert dfs_first_empty_path({'a': 'b'}) is None


def test_deferred_source():
    inc = dream.map(lambda n: n + 1)
    assert inc.of(range(3)).into(sum) == 6


def test_deferred_fn_terminated():
    incsum = dream.map(lambda n: n + 1).into(sum)
    assert incsum(range(3)) == 6


def test_composability():
    inc = dream.map(lambda n: n + 1)
    double = dream.map(lambda n: n * 2)
    assert inc.into(double).of(range(3)).into(set) == {2, 4, 6}


def test_of_files():
    assert dream.of_files('tests/testdata.txt').map(str.strip).into(list) == ['1', '2', '3']
    assert dream.of_files('tests/testd*.txt').count() == 6


Record = namedtuple('Record', ['id', 'count'])
def test_joined_dreams():
    recs1 = [Record(12, 34), Record(11, 123), Record(8, 5)]
    recs2 = [Record(11, 2), Record(8, 1), Record(3, 43)]
    joined_count = dream.of(recs1)\
        .join(recs2, lambda rec: rec.id)\
        .map(lambda rec: rec[0].count + rec[1].count)\
        .into(sum)
    assert joined_count == 123 + 2 + 5 + 1

    partial_joined = dream.join(recs2, lambda rec: rec.id) \
        .map(lambda rec: rec[0].count + rec[1].count) \
        .into(sum)
    assert partial_joined(recs1) == 123 + 2 + 5 + 1

    # # dask.bag does not support joining two bags
    # super_partial = dream.join(on=lambda rec: rec.id) \
    #     .map(lambda rec: rec[0].count + rec[1].count) \
    #     .into(sum)
    # assert super_partial(recs1, recs2) == 123 + 2 + 5 + 1


def test_fold():
    assert dream.of(range(3)).fold(add).compute() == sum(range(3))
    # assert dream.fold(add)(range(3)) == sum(range(3)) # TODO: need to overload bag.Item?


def test_foldby():
    assert dream.of(range(30)).foldby(lambda n: n % 2, add).into(dict) == {0: 210, 1: 225}

