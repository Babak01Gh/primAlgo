# Minimum Spanning Tree
creating minimum spanning tree using prim algorithm

**step1 :**
give for each vertix in graph infinity key value and parent None
except for start vertix (we take it the first one ('v1'))

**step2 :**
foreach other vertices in the graph if there is an edge between them (neighbor vertix)
we count the amount that we can arrive to the vertix by that.
we do this on every vertix one by one.

**step3 :**
give the minimum amount to each vertix's key and to it's parent is the vertix that we're checking it (u).
and finally we add (parent of vertix , vertix) double (minimums)
in solution array.
