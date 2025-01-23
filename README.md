# Assignment 2

Navigate to and open the notebook in colab.  Please
write your answers in there.

[Notebook](./solutions.ipynb)

## Question 1
Given the following undirected graph, perform a BFS as
well as DFS starting from vertex A. List the order in
which the vertices are visited.

$\\{A-B,\\; A-C,\\; B-D,\\; C-D,\\; D-E\\}$

## Question 2

Given the following directed graph, **algorithmically**
determine if it is a DAG. If it is not, explain why.

$\\{A\\to B,\\; B\\to C,\\; C\\to A,\\; B\\to D\\}$

## Question 3

Given the following DAG, **algorithmically** perform a
topological sort.  

$\\{A\\to B,\\; A\\to C,\\; B\\to D,\\; C\\to D\\}$

## Question 4

Given a weighted vertex graph $G(V,E)$, a start node
$s$ and a target sum $\sigma$.

**Write an algorithm, or equivalently a python program
(WAP)** to inspect if there is a path from $s$ such
that adding up all the vertex weights along the path,
equals the target sum.

Note: $\\forall v \\in V\\; \\exists v.w$ that
represents vertex weights.

## Question 5

**A binary tree** is a directed graph $G(V,E)$ with
following constraints,

1. $\\exists s\\in V$ such that $s$ is the unique root
   node.
2. $\\forall u\\in V,\\; \lvert E[u] \rvert \leqslant
   2$.
<!-- 2. $\\forall u\\in V,\\; E[u] \equiv \\{l,r\\}$ such -->
<!--    that $l.\mathrm{value} < u.\mathrm{value} < -->
<!--    r.\mathrm{value}$ -->

WAP to traverse a binary tree using BFS.  Illustrate
with necessary examples.

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
