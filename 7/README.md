Originally I tried to implement toposort using the "reverse finish time"
of a DFS traversal, as it is referred to by 15-210 at CMU. (Finish time
refers to when the recursive call returns.) This is the simplest and most
efficient algorithm for topological sorts.

Unfortunately that doesn't work, since you need to visit the alphabetically
least node at every step. The only solution, then, is to simulate the
visiting process by finding the alphabetically least node with indegree 0,
removing it from the graph, removing it, and then repeating. This is
basically what Kahn's algorithm is.

Part 2 reminded me of the Passport Control challenge from
[Bloomberg CodeCon](https://codecon.bloomberg.com/),
one instance of which took place at CMU not too long ago this Fall 2018.
