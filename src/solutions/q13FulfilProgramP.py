"""## Question 13 **[PY]**{: .htag } ##

Given $N$ courses labelled $\\{0,\\ldots,N-1\\}$ and a
list of prerequisites $R$ such that the courses
$R[i]\\equiv\\{a_i,b_i,\\ldots\\}$ are required to be
completed before enrolling for $i$-th course.

WAP to determine if all the $N$ courses can be
completed successfully by a candidate.  If so, also
determine one of the feasible ordering of courses.

**Examples**

1. $N=2$, $R=[\\emptyset,\\{0\\}]$ means that course $1$
   requires course $0$ as pre-requisite.  Hence, it is
   possible to complete the courses, in the following
   order: $[0,1]$.
2. $N=2$, $R=[\\{1\\},\\{0\\}]$. Here, the requirement is
   $1$ before $0$; and also $0$ before $1$.  This,
   hence, is impossible.

"""
def q13FulfilProgramP(R:List[List[int]]) :
  """
Args:
    R: A list of $N$ lists of integer values where the $i$-th list represents the reprequisites of $i$.
"""

  pass
