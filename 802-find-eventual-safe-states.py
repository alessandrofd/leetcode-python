"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1.
The graph is represented by a 0-indexed 2D integer array graph where graph[i]
is an integer array of nodes adjacent to node i, meaning there is an edge
from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe
node if every possible path starting from that node leads to a terminal node
(or another safe node).

Return an array containing all the safe nodes of the graph. The answer should
be sorted in ascending order.

Constraints:
    n == graph.length
    1 <= n <= 10^4
    0 <= graph[i].length <= n
    0 <= graph[i][j] <= n - 1
    graph[i] is sorted in a strictly increasing order.
    The graph may contain self-loops.
    The number of edges in the graph will be in the range [1, 4 * 10^4].
"""

from typing import List
from collections import defaultdict, deque

# Algoritmo de Kahn


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        reverse_graph = defaultdict(list)
        for i, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverse_graph[neighbor].append(i)
                indegree[i] += 1

        result = []
        queue = deque([node for node in range(n) if indegree[node] == 0])
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in reverse_graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted(result)


def test_solution():
    """test"""

    funcs = [
        Solution().eventualSafeNodes,
    ]

    # fmt: off
    data = [
        ([[1, 2], [2, 3], [5], [0], [5], [], []], [2,4,5,6]),
        ([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []], [4]),
    ]
    # fmt: on
    for graph, expected in data:
        for func in funcs:
            assert func(graph) == expected