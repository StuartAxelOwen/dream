*****
dream
*****

Dreamy data processing

Goals
=====

* Chained methods with functional flavor: ``dream.of(range(4)).map().filter().etc``
* Succinct creation of partial functions: ``inc = dream.map(lambda n: n + 1)``
* Multicore by default, simple single-core specification

And the stretch goal:

* Succinct simple function definition for dreams: ``from dream import dream, n; dream.map(n + 1)``

Radixes
=======

Radixes are essentially `fn.py <https://github.com/kachayev/fn.py>`_ _s, with a few more features and a few kinks worked out.  They let you describe simple functions in short hand:

.. code-block:: python
        
        >>> from dream import n
        >>> n % 4
        <dream.radix.Radix at 0x7f19281a3588>
        >>> (n % 4)(10)
        2

They let you do interesting things without needing a whole lambda.

.. code-bock:: python
        
        >>> from dream import s
        >>> dream.of('Hello, gorgeous.').map(s.upper).filter(s.

**Things You Can't Do**

Due to so design choices in some Python magic methods, you can't do the following:

.. code-block:: python

	(hash(a))('yo')  # This would make most membership checks of radices impossible 

	(not a)(False)  # __nonzero__ must return a bool (corced to bool by not)

	(bool(a))(False)  # __nonzero__ must return a bool

	(int(a))('4')
