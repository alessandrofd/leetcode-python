"""
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and
an array edges where edges[i] = [fromi, toi] represents a directed edge from
node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are
reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

Constraints:
    2 <= n <= 10^5
    1 <= edges.length <= min(10^5, n * (n - 1) / 2)
    edges[i].length == 2
    0 <= fromi, toi < n
    All pairs (fromi, toi) are distinct.
"""
from typing import List

class Solution:
    def findSmallestSetOfVertices(self, num_nodes: int, edges: List[List[int]]) -> List[int]:
        reached_nodes = {node for _, node in edges}
        return [node for node in range(num_nodes) if node not in reached_nodes]


def test_solution():
    """test"""

    funcs = [
        Solution().findSmallestSetOfVertices,
    ]

    data = [
        (6, [[0,1],[0,2],[2,5],[3,4],[4,2]], [0,3]),
        (5, [[0,1],[2,1],[3,1],[1,4],[2,4]], [0,2,3]),
    ]

    for num_nodes, edges, expected in data:
        for func in funcs:
            assert func(num_nodes, edges) == expected
