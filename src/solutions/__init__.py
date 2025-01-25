from collections import namedtuple
from enum import Enum

Graph = namedtuple("Graph", "V,E")
"""Graph DataType. 

Essentially a namedtuple with members accessible as
attributes.  So that `G.V` and `G.E` represent list of
verts and adjacency respectively.
"""

Bbt = Enum('Bbt', 'False,True,OR,AND')
"""Enumeration for constants in a Boolean Binary Tree.

This is just a fancy way of assigning the following
constants, without polluting the global namespace,

``` python
Bbt.False = 0    # constant
Bbt.True = 1     # constant
Bbt.OR = 2       # constant
Bbt.AND = 3      # constant
```

"""

Flight = namedtuple("Flight", "s,d,p")
"""Flight DataType. 

Essentially a namedtuple with members accessible as
attributes, i.e. `F.s`, `F.d` and `F.p`.

Args:
  s: Source City.
  d: Destination City.
  p: Cost Price of the flight.
"""
