"""## Question 16 ##

There’s a dungeon arranged as a grid of $N\\times M$
rectangular rooms.

$T\\in\\mathbb{Z}^{N\\times M}$ represents for each room
$(i,j)$, a threshold of **minimum** time $t_{ij}$
starting from which a **move into** it may be
initiated.

**Move** is allowed only between two **adjacent** rooms
that share a common *vertical* or *horizontal* wall,
and each move takes **1 unit** time duration.

WAP to start from room $(0,0)$ and finally determine
the minimum time required to reach the room
$(N-1,M-1)$.

**Examples**

1. $T=[[0,4],[4,4]]$  
   Result: $6$  
   Explanation:  
   $t=4: (0,0)\\to(1,0)$;  
   $t=5: (1,0)\\to(1,1)$.
2. $T=[[0,0,0],[0,0,0]]$  
   Result: $3$  
   Explanation:  
   $t=0: (0,0)\\to(1,0)$;  
   $t=1: (1,0)\\to(1,1)$;  
   $t=1: (1,1)\\to(1,1)$.
2. $T=[[0,1],[1,2]]$  
   Result: $3$  
   Explanation:  
   $t=1: (0,0)\\to(1,0)$;  
   $t=2: (1,0)\\to(1,1)$.

"""
def q16DungeonCrossingTimeMin(T:List[List[int]]) :
  """
Args:
  T: A list of $N$ lists of $M$ integer values each representing threshold time at room $(i,j)$.

"""

  pass
