__author__ = 'stuart'

import sys
from .dream3 import Dream

class EmptyDream(object):
    def __getattribute__(self, name):
        return globals().get(name) or Dream().__getattribute__(name)

# Masquerade ``EmptyDream`` as module to allow ``import dream; dream.map(stuff)``
sys.modules[__name__] = EmptyDream()
