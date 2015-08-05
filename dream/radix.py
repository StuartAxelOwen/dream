__author__ = 'stuart'


class Radix(object):
    # def __new__(cls, *args, **kwargs):
    #     return list.__new__(cls, *args, **kwargs)

    def __init__(self, accessor=lambda x: x):
        self._accessor = accessor

    def __call__(self, *args, **kwargs):
        return Radix(lambda thing: self._accessor(thing)(*args, **kwargs))

    def _dream(self, *args, **kwargs):
        return self._accessor(*args, **kwargs)

    def __getitem__(self, name):
        return Radix(lambda thing: self._accessor(thing).__getitem__(name))

    def __len__(self):
        return Radix(lambda thing: self._accessor(thing).__len__())

    def __setitem__(self, key, value):
        return Radix(lambda thing: self._accessor(thing).__setitem__(key, value))

    def __delitem__(self, key):
        return Radix(lambda thing: self._accessor(thing).__delitem__(key))

    # def __iter__(self):
    #     return Radix(lambda thing: self._accessor(thing).__iter__())

    def __reversed__(self):
        return Radix(lambda thing: self._accessor(thing).__reversed__())

    def __contains__(self, other):
        print("calling contains")
        result = IntRadix(lambda thing: self._accessor(thing).__contains__(other))
        # print(result._dream)
        # print(dir(result))
        return result

    def __missing__(self, key):
        return Radix(lambda thing: self._accessor(thing).__missing__(key))

    def __getattr__(self, name):
        print("Getting attr {}".format(name))
        return Radix(lambda thing: self._accessor(thing).__getattribute__(name))

    def __add__(self, other):
        return Radix(lambda thing: self._accessor(thing).__add__(other))

    def __sub__(self, other):
        return Radix(lambda thing: self._accessor(thing).__sub__(other))

    def __mul__(self, other):
        return Radix(lambda thing: self._accessor(thing).__mul__(other))

    def __div__(self, other):
        return Radix(lambda thing: self._accessor(thing).__div__(other))

    def __truediv__(self, other):
        return Radix(lambda thing: self._accessor(thing).__truediv__(other))

    def __floordiv__(self, other):
        return Radix(lambda thing: self._accessor(thing).__floordiv__(other))

    def __mod__(self, other):
        return Radix(lambda thing: self._accessor(thing).__mod__(other))

    def __divmod__(self, other):
        return Radix(lambda thing: self._accessor(thing).__divmod__(other))

    def __pow__(self, power, modulo=None):
        print(power, modulo)
        return Radix(lambda thing: self._accessor(thing).__pow__(power, modulo))

    def __lshift__(self, other):
        return Radix(lambda thing: self._accessor(thing).__lshift__(other))

    def __rshift__(self, other):
        return Radix(lambda thing: self._accessor(thing).__rshift__(other))

    def __and__(self, other):
        return Radix(lambda thing: self._accessor(thing).__and__(other))

    def __or__(self, other):
        return Radix(lambda thing: self._accessor(thing).__or__(other))

    def __xor__(self, other):
        return Radix(lambda thing: self._accessor(thing).__xor__(other))

    def __radd__(self, other):
        return Radix(lambda thing: self._accessor(thing).__add__(other))

    def __rsub__(self, other):
        return Radix(lambda thing: self._accessor(thing).__sub__(other))

    def __rmul__(self, other):
        return Radix(lambda thing: self._accessor(thing).__mul__(other))

    def __rdiv__(self, other):
        return Radix(lambda thing: self._accessor(thing).__div__(other))

    def __rtruediv__(self, other):
        return Radix(lambda thing: self._accessor(thing).__truediv__(other))

    def __rfloordiv__(self, other):
        return Radix(lambda thing: self._accessor(thing).__floordiv__(other))

    def __rmod__(self, other):
        return Radix(lambda thing: self._accessor(thing).__mod__(other))

    def __rdivmod__(self, other):
        return Radix(lambda thing: self._accessor(thing).__divmod__(other))

    def __rpow__(self, power, modulo=None):
        return Radix(lambda thing: self._accessor(thing).__pow__(power, modulo))

    def __rlshift__(self, other):
        return Radix(lambda thing: self._accessor(thing).__lshift__(other))

    def __rrshift__(self, other):
        return Radix(lambda thing: self._accessor(thing).__rshift__(other))

    def __rand__(self, other):
        return Radix(lambda thing: self._accessor(thing).__and__(other))

    def __ror__(self, other):
        return Radix(lambda thing: self._accessor(thing).__or__(other))

    def __rxor__(self, other):
        return Radix(lambda thing: self._accessor(thing).__xor__(other))

    def __eq__(self, other):
        return Radix(lambda thing: self._accessor(thing).__eq__(other))

    def __ne__(self, other):
        return Radix(lambda thing: self._accessor(thing).__ne__(other))

    def __gt__(self, other):
        return Radix(lambda thing: self._accessor(thing).__gt__(other))

    def __lt__(self, other):
        return Radix(lambda thing: self._accessor(thing).__lt__(other))

    def __ge__(self, other):
        return Radix(lambda thing: self._accessor(thing).__ge__(other))

    def __le__(self, other):
        return Radix(lambda thing: self._accessor(thing).__le__(other))

    def __pos__(self):
        return Radix(lambda thing: self._accessor(thing).__pos__())

    def __neg__(self):
        return Radix(lambda thing: self._accessor(thing).__neg__())

    def __abs__(self):
        return Radix(lambda thing: self._accessor(thing).__abs__())

    def __invert__(self):
        return Radix(lambda thing: self._accessor(thing).__invert__())

    def __round__(self, n=0):
        print("calling")
        return Radix(lambda thing: self._accessor(thing).__round__(n))

    def __floor__(self):
        return Radix(lambda thing: self._accessor(thing).__floor__())

    def __ceil__(self):
        return Radix(lambda thing: self._accessor(thing).__ceil__())

    def __unicode__(self):
        return Radix(lambda thing: self._accessor(thing).__unicode__())

    def __format__(self):
        return Radix(lambda thing: self._accessor(thing).__format__())

    def __hash__(self):
        return hash(self._accessor)

    def __reduce__(self):
        return (Radix, (self._accessor, ))

    def __sizeof__(self):
        return Radix(lambda thing: self._accessor(thing).__sizeof__())

    def __signature__(self):
        raise AttributeError


class IntRadix(Radix, int):
    def __new__(cls, *args, **kwargs):
        print("Calling IntRadix new")
        print(type(Radix.__new__))
        print(args)
        print(kwargs)
        self = int.__new__(IntRadix, 0)
        return self

    def __init__(self, accessor=lambda x: x):
        print("IntRadix init")
        self._accessor = accessor

    # def __getattribute__(self, key):
    #     print("getting " + key)

a, b, c, d, e, f, g, h, i, j, k, l, m = (Radix() for _ in range(13)) 
n, o, p, q, r, s, t, u, v, w, x, y, z = (Radix() for _ in range(13))
_ = Radix()
