__author__ = 'stuart'

from dream.radix import a, b, c, d
import math


def test_radix_math_basic():
    assert (a + 1)(2) == 3
    assert (a - 1)(3) == 2
    assert (a * 2)(6) == 12
    assert (a / 4)(10) == 2.5
    assert (a // 4)(10) == 2
    assert (a ** 2)(3) == 9
    assert (a % 5)(13) == 3

def test_radix_math_complex():
    assert ((a + 1) * 2)(0) == 2

def test_radix_math_reflected():
    assert (a + 1)(2) == 3
    assert (a - 1)(3) == 2
    assert (a * 2)(6) == 12
    assert (a / 4)(10) == 2.5
    assert (a // 4)(10) == 2
    assert (a ** 2)(3) == 9
    assert (a % 5)(13) == 3

def test_radix_accessor_basic():
    assert (a[0])([12]) == 12
    assert (a[-1])([1, 2, 3]) == 3
    assert (a[:3])([0, 1, 2, 3, 4]) == [0, 1, 2]
    assert (a['b'])({'b': 2}) == 2
    assert (a[None])({None: 13}) == 13

def test_radix_comparisons_basic():
    assert (a < 1)(0)
    assert not (a < 1)(1)
    assert (a > 1)(2)
    assert not (a > 1)(0)
    assert (a <= 1)(0)
    assert (a <= 1)(1)
    assert not (a <= 1)(2)
    assert (a >= 1)(1)
    assert (a >= 1)(2)
    assert not (a >= 1)(0)
    assert (a == 1)(1)
    assert not (a == 1)(0)
    assert (a != 0)(1)
    assert not (a != 0)(0)

def test_radix_comparisons_fancy():
    # assert ((a < 1).inv)(1)
    pass

def test_radix_unary_ops_basic():
    assert (+a)(-12) == (-12).__pos__()
    assert (-a)(13) == (13).__neg__()
    assert (abs(a))(-21) == (-21).__abs__()
    assert (~a)(5) == ~5
    assert (round(a, 2))(2.555) == round(2.555, 2)
    # assert (math.floor(a))(2.7) == 2
    # assert (math.ceil(a))(2.3) == 3
    assert (math.trunc(a))(2.5) == 2

def test_radix_and_or_basic():
    assert (a | 5)(1) == 5 | 1
    assert (a | 4)(7) == 4 | 7

    assert (a & 5)(1) == 5 & 1
    assert (a & 4)(7) == 4 & 7

    assert (a ^ 5)(1) == 5 ^ 1
    assert (a ^ 4)(7) == 4 ^ 7

def test_radix_and_or_reflected():
    assert (5 | a)(1) == 5 | 1
    assert (4 | a)(7) == 4 | 7

    assert (5 & a)(1) == 5 & 1
    assert (4 & a)(7) == 4 & 7

    assert (5 ^ a)(1) == 5 ^ 1
    assert (4 ^ a)(7) == 4 ^ 7

def test_multiple_radixes_math():
    assert (a + b)(1, 2) == 3

def test_things_i_actually_want():
    # d = {}
    # d[1] = {'a': 'blam'}
    assert (a.set(1, {'a': 'blam'}))({}) == {1: {'a': 'blam'}}
