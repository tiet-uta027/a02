"""## Question 15 **[PY]**{: .htag } ##

There are $N$ cities, connected by flights.  Given the
list of flights $F\\equiv\\{(s_i,d_i,p_i):0<i\\leqslant
N\\}$ so that $i$-th flight connects the source city
$s_i$ to destination city $d_i$ for a cost-price of
$p_i$.

Given $A,B,k$, WAP to determine **the cheapest price**
to connect city $A$ to city $B$ with maximum $k$ stops.

![](./assets/flights.png)

**Examples** (Optimal paths marked in red)

1. $N=4, F\\equiv\\{ (0,1,100), (1,2,100), (2,0,100),
   (2,3,200) \\}, A=0, B=3, k=1$  
   Result: $700$
2. $N=3, F\\equiv \\{ (0,1,100), (1,2,100), (0,2,500) \\},
   A=0, B=2, k=1$  
   Result: $200$
2. $N=3, F\\equiv \\{ (0,1,100), (1,2,100), (0,2,500) \\},
   A=0, B=2, k=0$  
   Result: $500$

See also: [Flight](../#flight)
"""
from . import Graph,Bbt,Flight
def q15GetCheapestFlight(
    F: List[Flight],
    cityA: int,
    cityB: int,
    k: int
) :
  """
Args:
  F: List of [`Flight`](../#flight)s.
  cityA: Source city.
  cityB: Destination city.
  k: Num hops permissible in travel.

"""

  pass
