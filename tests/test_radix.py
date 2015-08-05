__author__ = 'stuart'

from dream.radix import a, b, c, d
import math


def test_radix_math_basic():
    assert (a + 1)._dream(2) == 3
    assert (a - 1)._dream(3) == 2
    assert (a * 2)._dream(6) == 12
    assert (a / 4)._dream(10) == 2.5
    assert (a // 4)._dream(10) == 2
    assert (a ** 2)._dream(3) == 9
    assert (a % 5)._dream(13) == 3

def test_radix_math_complex():
    assert ((a + 1) * 2)(0) == 2

def test_radix_math_reflected():
    assert (1 + a)._dream(2) == 3
    assert (1 - a)._dream(3) == -2
    assert (2 * a)._dream(6) == 12
    assert (4 / a)._dream(10) == 0.4
    assert (4 // a)._dream(2) == 2
    assert (2 ** a)._dream(3) == 8
    assert (13 % a)._dream(5) == 3

def test_radix_accessor_basic():
    assert (a[0])._dream([12]) == 12
    assert (a[-1])._dream([1, 2, 3]) == 3
    assert (a[:3])._dream([0, 1, 2, 3, 4]) == [0, 1, 2]
    assert (a['b'])._dream({'b': 2}) == 2
    assert (a[None])._dream({None: 13}) == 13

def test_radix_comparisons_basic():
    assert (a < 1)._dream(0)
    assert not (a < 1)._dream(1)
    assert (a > 1)._dream(2)
    assert not (a > 1)._dream(0)
    assert (a <= 1)._dream(0)
    assert (a <= 1)._dream(1)
    assert not (a <= 1)._dream(2)
    assert (a >= 1)._dream(1)
    assert (a >= 1)._dream(2)
    assert not (a >= 1)._dream(0)
    assert (a == 1)._dream(1)
    assert not (a == 1)._dream(0)
    assert (a != 0)._dream(1)
    assert not (a != 0)._dream(0)

def test_radix_comparisons_fancy():
    # assert ((a < 1).inv)(1)
    pass

def test_radix_contains():
    assert('a' in a)._dream({'a', 'b', 'c'})
    assert('a' in a)._dream({'b', 'c'})

def test_radix_unary_ops_basic():
    assert (+a)._dream(-12) == (-12).__pos__()
    assert (-a)._dream(13) == (13).__neg__()
    assert (abs(a))._dream(-21) == (-21).__abs__()
    assert (~a)._dream(5) == ~5
    assert (round(a, 2))._dream(2.555) == round(2.555, 2)
    # assert (math.floor(a))(2.7) == 2
    # assert (math.ceil(a))(2.3) == 3
    assert (math.trunc(a))._dream(2.5) == 2

def test_radix_and_or_basic():
    assert (a | 5)._dream(1) == 5 | 1
    assert (a | 4)._dream(7) == 4 | 7

    assert (a & 5)._dream(1) == 5 & 1
    assert (a & 4)._dream(7) == 4 & 7

    assert (a ^ 5)._dream(1) == 5 ^ 1
    assert (a ^ 4)._dream(7) == 4 ^ 7

def test_radix_and_or_reflected():
    assert (5 | a)._dream(1) == 5 | 1
    assert (4 | a)._dream(7) == 4 | 7

    assert (5 & a)._dream(1) == 5 & 1
    assert (4 & a)._dream(7) == 4 & 7

    assert (5 ^ a)._dream(1) == 5 ^ 1
    assert (4 ^ a)._dream(7) == 4 ^ 7

def test_multiple_radixes_math():
    assert (a + b)._dream(1, 2) == 3

def test_things_i_actually_want():
    # d = {}
    # d[1] = {'a': 'blam'}
    assert (a[1] = {'a': 'blam'})._dream({}) == {1: {'a': 'blam'}}

def test_radix_method_calls():
    assert (a.upper())._dream('hi') == 'HI'
    assert (a.encode('utf-8'))._dream('a') == b'a'
