=====
dream
=====

dream is a composition tool for task graphs - `dasks <https://github.com/continuumio/dask>`_, specifically.

Goals
=====

* Chained methods with functional flavor: 
  :: 
      
      dream.of(range(4)).map().filter().etc
      
* Succinct creation of partial functions: 
  ::
  
      inc = dream.map(lambda n: n + 1); evens = dream.filter(lambda n: n % 2 == 0)
      
      
* Composable into more complex graphs: 
  ::
  
      inc.into(events).of(range(4)).into(set) == {2, 4}

And the stretch goal:

* Succinct simple function definition for dreams: 
  ::
      
      from dream import dream, n; dream.map(n + 1)``
