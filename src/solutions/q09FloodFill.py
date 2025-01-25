"""## Question 9 **[PY]**{: .htag } ##

Given an image $M\\in\\mathbb{Z}^{H\\times W}$ represented
as a grid (or matrix) of $H\\times W$ of integers, where
$m_{ij}$ represents the pixel value of $i$-th row,
$j$-th column.

1. WAP to flood-fill colour $\\kappa$ starting at pixel
   at $r$-th row and $c$-th column.
   
2. Reflect on the relative merits of using BFS/DFS for
   the process.

**Flood Fill**

* Flood fill is a process to change the colour of a
  contiguous region, by starting with a given source
  pixel and expanding along the neighbours until a
  boundary is hit.
* Region is defined by colour of the start pixel.
* Neighbours shares a boundary (either vertically or
  horizontally).
* A neighbour with colour different than that of the
  start pixel is deemed to be a boundary; it’s colour
  is left untouched!

"""
def q09FloodFill(M:List[List[int]],k:int,r:int,c:int) :
  """
Args:
  M: A list of $H$ lists of $W$ integer values each representing colour at pixel $(i,j)$.
  k: Target colour.
  r: Row of the start pixel.
  c: Col of the start pixel.
"""

  pass
