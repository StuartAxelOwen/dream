__author__ = 'stuart'

import dream
from dream import a, n, d, s


"""
# Czecklist

1. Able to access attributes and items using radix (thoughts?)
  - DONE
2. Able to call methods using radix (thoughts?)
  - DONE
3. Able to call functions on radix (thought?)... (lol maybe impossible)
  - This might be best as `dream.of(things).map(s.split())
  - Holy shit - if you could invert program flow... fucking brainception going on right now

Announcement tweet:

from dream import dream, n
dream.of(range(1000)).filter(n**0.5 % 1 == 0).into(list)


"""


print((s.upper())._dream('a'))
assert (s.upper() == 'A')._dream('a')

dreamt = dream.of(range(10)).map(lambda n: n - n % 3)
print(type(dreamt))
print(dreamt.collect())

joiner = dream.map(str).into('\t'.join)

print(joiner(range(5)))
print(joiner(range(2)))

x = [list(range(i)) for i in range(4, 10)]
print(x)
print(dream.of(x).map(joiner).collect())
