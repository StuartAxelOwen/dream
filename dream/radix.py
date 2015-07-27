__author__ = 'stuart'


class Radix(object):
    __magic_methods = {'__add__', '__sub__', '__mul__', '__div__'}

    def __init__(self, accessor=lambda x: x):
        self.accessor = accessor

    def __call__(self, *args, **kwargs):
        return self.accessor(*args, **kwargs)

    def __getitem__(self, name):
        return Radix(lambda thing: self.accessor(thing).__getitem__(name))

    def __getattr__(self, name):
        print("Getting attr {}".format(name))
        return Radix(lambda thing: self.accessor(thing).__getattribute__(name))

    def __add__(self, other):
        return Radix(lambda thing: self.accessor(thing).__add__(other))

    def __sub__(self, other):
        return Radix(lambda thing: self.accessor(thing).__sub__(other))

    def __mul__(self, other):
        return Radix(lambda thing: self.accessor(thing).__mul__(other))

    def __div__(self, other):
        return Radix(lambda thing: self.accessor(thing).__div__(other))

    def __truediv__(self, other):
        return Radix(lambda thing: self.accessor(thing).__truediv__(other))

    def __floordiv__(self, other):
        return Radix(lambda thing: self.accessor(thing).__floordiv__(other))

    def __mod__(self, other):
        return Radix(lambda thing: self.accessor(thing).__mod__(other))

    def __divmod__(self, other):
        return Radix(lambda thing: self.accessor(thing).__divmod__(other))

    def __pow__(self, power, modulo=None):
        return Radix(lambda thing: self.accessor(thing).__pow__(power, modulo))

    def __lshift__(self, other):
        return Radix(lambda thing: self.accessor(thing).__lshift__(other))

    def __rshift__(self, other):
        return Radix(lambda thing: self.accessor(thing).__rshift__(other))

    def __and__(self, other):
        return Radix(lambda thing: self.accessor(thing).__and__(other))

    def __or__(self, other):
        return Radix(lambda thing: self.accessor(thing).__or__(other))

    def __xor__(self, other):
        return Radix(lambda thing: self.accessor(thing).__xor__(other))

    def __radd__(self, other):
        return Radix(lambda thing: self.accessor(thing).__add__(other))

    def __rsub__(self, other):
        return Radix(lambda thing: self.accessor(thing).__sub__(other))

    def __rmul__(self, other):
        return Radix(lambda thing: self.accessor(thing).__mul__(other))

    def __rdiv__(self, other):
        return Radix(lambda thing: self.accessor(thing).__div__(other))

    def __rtruediv__(self, other):
        return Radix(lambda thing: self.accessor(thing).__truediv__(other))

    def __rfloordiv__(self, other):
        return Radix(lambda thing: self.accessor(thing).__floordiv__(other))

    def __rmod__(self, other):
        return Radix(lambda thing: self.accessor(thing).__mod__(other))

    def __rdivmod__(self, other):
        return Radix(lambda thing: self.accessor(thing).__divmod__(other))

    def __rpow__(self, power, modulo=None):
        return Radix(lambda thing: self.accessor(thing).__pow__(power, modulo))

    def __rlshift__(self, other):
        return Radix(lambda thing: self.accessor(thing).__lshift__(other))

    def __rrshift__(self, other):
        return Radix(lambda thing: self.accessor(thing).__rshift__(other))

    def __rand__(self, other):
        return Radix(lambda thing: self.accessor(thing).__and__(other))

    def __ror__(self, other):
        return Radix(lambda thing: self.accessor(thing).__or__(other))

    def __rxor__(self, other):
        return Radix(lambda thing: self.accessor(thing).__xor__(other))

    def __eq__(self, other):
        return Radix(lambda thing: self.accessor(thing).__eq__(other))

    def __ne__(self, other):
        return Radix(lambda thing: self.accessor(thing).__ne__(other))

    def __gt__(self, other):
        return Radix(lambda thing: self.accessor(thing).__gt__(other))

    def __lt__(self, other):
        return Radix(lambda thing: self.accessor(thing).__lt__(other))

    def __ge__(self, other):
        return Radix(lambda thing: self.accessor(thing).__ge__(other))

    def __le__(self, other):
        return Radix(lambda thing: self.accessor(thing).__le__(other))

    def __pos__(self):
        return Radix(lambda thing: self.accessor(thing).__pos__())

    def __neg__(self):
        return Radix(lambda thing: self.accessor(thing).__neg__())

    def __abs__(self):
        return Radix(lambda thing: self.accessor(thing).__abs__())

    def __invert__(self):
        return Radix(lambda thing: self.accessor(thing).__invert__())

    def __round__(self, n=0):
        return Radix(lambda thing: self.accessor(thing).__round__(n))

    def __floor__(self):
        return Radix(lambda thing: self.accessor(thing).__floor__())

    def __ceil__(self):
        return Radix(lambda thing: self.accessor(thing).__ceil__())

    def __unicode__(self):
        return Radix(lambda thing: self.accessor(thing).__unicode__())

    def __format__(self):
        return Radix(lambda thing: self.accessor(thing).__format__())

    def __hash__(self):
        return Radix(lambda thing: self.accessor(thing).__hash__())

    def __dir__(self):
        return Radix(lambda thing: self.accessor(thing).__dir__())

    def __sizeof__(self):
        return Radix(lambda thing: self.accessor(thing).__sizeof__())

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = (Radix() for _ in range(26))

