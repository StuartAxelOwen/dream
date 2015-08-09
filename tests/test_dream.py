
# import dream.dream3 as dream
import dream
from dream.dream import Empty, dfs_first_empty_path


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


def test_deferred_source():
    inc = dream.map(lambda n: n + 1)
    assert inc.of(range(3)).into(sum) == 6


def test_composability():
    inc = dream.map(lambda n: n + 1)
    double = dream.map(lambda n: n * 2)
    assert inc.into(double).of(range(3)).into(set) == {2, 4, 6}


def test_of_files():
    assert dream.of_files('tests/testdata.txt').map(str.strip).into(list) == ['1', '2', '3']
    assert dream.of_files('tests/testd*.txt').count() == 6
