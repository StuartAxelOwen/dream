
# import dream.dream3 as dream
import dream
from dream.dream3 import Nothing, dfs_first_nothing_path
from operator import add

def test_map_basic():
    assert dream.of(range(4)).map(lambda n: n + 1).into(sum) == 10
    assert dream.of(range(4)).into(sum) == 6

def test_filter_basic():
    assert dream.of(range(4)).filter(lambda n: n % 2 == 0).into(sum) == 2

def test_dfs_nothing_search():
    dsk = {'a': Nothing}
    assert dfs_first_nothing_path(dsk) == ['a']
    dsk = {'a': {'b': 1}, 'c': {None: Nothing}}
    assert dfs_first_nothing_path(dsk) == ['c', None]

def test_deferred_source():
    inc = dream.map(lambda n: n + 1)
    assert inc.of(range(3)).into(tuple) == (1, 2, 3)

def test_composability():
    inc = dream.map(lambda n: n + 1)
    double = dream.map(lambda n: n * 2)
    assert inc.into(double).of(range(3)).into(tuple) == (2, 4, 6)

def test_of_files():
    assert dream.of_files('tests/testdata.txt').map(str.strip).into(list) == ['1', '2', '3']
