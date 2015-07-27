__author__ = 'stuart'

import dream


dreamt = dream.of(range(10)).map(lambda n: n - n % 3)
print(type(dreamt))
print(dreamt.collect())

joiner = dream.map(str).to('\t'.join)

print(joiner(range(5)))
print(joiner(range(2)))

x = [list(range(i)) for i in range(4, 10)]
print(x)
print(dream.of(x).map(joiner).collect())
