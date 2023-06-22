"""
There is an undirected graph with n nodes, where each node is numbered
between 0 and n - 1. You are given a 2D array graph, where graph[u] is
an array of nodes that node u is adjacent to. More formally, for each v in
graph[u], there is an undirected edge between node u and node v. The graph
has the following properties:

    There are no self-edges (graph[u] does not contain u).

    There are no parallel edges (graph[u] does not contain duplicate values).

    If v is in graph[u], then u is in graph[v] (the graph is undirected).

    The graph may not be connected, meaning there may be two nodes u and v
    such that there is no path between them.

A graph is bipartite if the nodes can be partitioned into two independent
sets A and B such that every edge in the graph connects a node in set A and
a node in set B.

Return true if and only if it is bipartite.

Constraints:
    graph.length == n
    1 <= n <= 100
    0 <= graph[u].length < n
    0 <= graph[u][i] <= n - 1
    graph[u] does not contain u.
    All the values of graph[u] are unique.
    If graph[u] contains v, then graph[v] contains u.
"""

# A cada nó, os seus nós adjacentes não podem estar concectados entre si.
# Essa é uma condição necessári
# a mas não suficiente. Pode exmplo, se houver
# um ciclo com número ímpar de elementos o grafo não será bipartite apesar
# da condição dos adjacentes de um mesmo nó não estarem conectados entre si.

# Podemos criar grupos distribuir os nós nestes grupos

from typing import List

class Solution:
    def isBipartite_stack(self, graph: List[List[int]]) -> bool:
        return True

    def isBipartite_recurse(self, graph: List[List[int]]) -> bool:
        return True


def test_solution():
    """test"""

    funcs = [
        Solution().isBipartite_recurse,
        Solution().isBipartite_stack,
    ]

    data = [
        ([ [1, 2, 3], [0, 2], [0, 1, 3], [0, 2], ], False),
        ([ [1, 3], [0, 2], [1, 3], [0, 2], ], True),
        ([ [4, 1], [0, 2], [1, 3], [2, 4], [3, 0], ], False),
    ]

    for graph, expected in data:
        for func in funcs:
            assert func(graph) == expected
