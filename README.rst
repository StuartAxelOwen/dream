=====
dream
=====

Dreamy data processing

Radixes
-------

Things You Can't Do

Due to so design choices in some Python magic methods, you can't do the following:

.. code-block:: python

	(hash(a))('yo')  # This would make most membership checks of radices impossible 

	(not a)(False)  # __nonzero__ must return a bool (corced to bool by not)

	(bool(a))(False)  # __nonzero__ must return a bool

	(int(a))('4')
