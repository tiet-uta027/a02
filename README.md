# Assignment 2

Navigate to and open the notebook in colab.  Please
write your answers in there.

[Notebook](./solutions.ipynb)

## Question 1
Given the following undirected graph, perform a BFS as
well as DFS starting from vertex A. List the order in
which the vertices are visited.

$\{A-B,\; A-C,\; B-D,\; C-D,\; D-E\}$

## Question 2

Given the following directed graph, **algorithmically**
determine if it is a DAG. If it is not, explain why.

$\{A\to B,\; B\to C,\; C\to A,\; B\to D\}$

## Question 3

Given the following DAG, **algorithmically** perform a
topological sort.  

$\{A\to B,\; A\to C,\; B\to D,\; C\to D\}$

## Question 4

Given a weighted vertex graph $G(V,E)$, a start node
$s$ and a target sum $\sigma$.

**Write an algorithm, or equivalently a python program
(WAP)** to inspect if there is a path from $s$ such
that adding up all the vertex weights along the path,
equals the target sum.

Note: $\forall v \in V\; \exists v.w$ that
represents vertex weights.

## Question 5

WAP to traverse [a binary tree](#binary-tree "Glossary
for Binary Tree") using BFS.  Illustrate with necessary
examples.

## Question 6 ##

Given two binary trees, $A,B$, WAP to compute a merge
operation defined as follows:

Imagine that one is put on to cover the other; some
nodes overlap, while others don’t.  The merge rule
states that for each position in the binary tree, if
two nodes overlap, the value of the merged node is
their sum; otherwise, it’s the value of not null
node. _E.g._

![](./assets/q6.png)

## Question 7 ##

If the following paths completely describe a given
**undirected** graph, show one possible order of nodes
visited through BFS.

$M-N-O-P-Q$  
$N-Q-M-R$

## Question 8 ##

Given a binary tree, $B$ find its min, max and average
depths.

**PS:** Depth of a tree is defined by the distance of
leaf nodes from the root.

## Question 9 ##

Given an image $M\in\mathbb{Z}^{H\times W}$ represented
as a grid (or matrix) of $H\times W$ of integers, where
$m_{ij}$ represents the pixel value of $i$-th row,
$j$-th column.

1. WAP to flood-fill colour $\kappa$ starting at pixel
   at $s_r$-th row and $s_c$-th column.
   
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
  
[LeetCode #733][LC733]

## Question 10 ##

Given an undirected graph $G(V,E)$ without
[self-loops][LOOP], and a pair $(s,d)$ of source and
destination vertices, determine if a path between them
exists in the graph.

## Question 11 ##

**Evaluate a Boolean Binary Tree**

Given a full binary tree $B$ such that,
+ Leaf nodes bear binary truth values, i.e. `True` or
  `False`; and 
+ Non leaf nodes bear values that represent logic
  gates, namely `AND` or `OR`.
  
WAP to evaluate the boolean binary tree $B$ and return
the result.

![](./assets/boolean-binary-tree.png "Example Boolean
Binary Tree")

## Question 12 ##

**Island Perimeter**

Given a binary rectangular grid $M\in\{0,1\}^{H\times
W}$ with $H$ rows and $W$ columns, where each pixel
$m_{ij}$ represents either $0$ for water or $1$ for
land.  Assume _a)_ that there’s exactly one island
(contiguously connected land cells), _b)_ that pixels
are connected either vertically or horizontally but not
diagonally, and _c)_ that there’re no lakes.

WAP to determine the perimeter of the island!

[LeetCode #463][LC463]

## Glossary ##

### Loop ###

An edge from a vertex to its own self.

### Binary Tree ###

A directed graph, where

+ There’s a fixed start node called **root**;
+ Each node may have upto two children; and
+ The node with no children is called a **leaf**.

### Full Binary Tree ###

A binary tree where each node has either two or no children

<!-- *[WAP]: Write a program or equivalently a python code -->

[LC733]: https://leetcode.com/problems/flood-fill/ "LeetCode Problem #733"

[LC463]: https://leetcode.com/problems/island-perimeter/ "LeetCode Problem #463"

[LOOP]: https://en.wikipedia.org/wiki/Loop_(graph_theory) "Loop in Graph Theory"
