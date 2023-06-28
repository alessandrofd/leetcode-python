"""
You are given an undirected weighted graph of n nodes (0-indexed),
represented by an edge list where edges[i] = [a, b] is an undirected edge
connecting the nodes a and b with a probability of success of traversing that
edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of
success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted
if it differs from the correct answer by at most 1e-5.

Constraints:
    2 <= n <= 10^4
    0 <= start, end < n
    start != end
    0 <= a, b < n
    a != b
    0 <= succProb.length == edges.length <= 2*10^4
    0 <= succProb[i] <= 1
    There is at most one edge between every two nodes.
"""
from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succ_prob: List[float],
        start: int,
        end: int,
    ) -> float:
        """Dijkstra's Algorithm"""

        return 0.0


def test_solution():
    """test"""

    funcs = [
        Solution().maxProbability,
    ]

    # fmt: off
    data = [
        (3, [ [0, 1], [1, 2], [0, 2], ], [0.5, 0.5, 0.2], 0, 2, 0.25000),
        (3, [ [0, 1], [1, 2], [0, 2], ], [0.5, 0.5, 0.3], 0, 2, 0.30000),
        (3, [[0, 1]], [0.5], 0, 2, 0.00000),
    ]
    # fmt: on
    for n, edges, succ_prob, start, end, expected in data:
        for func in funcs:
            assert func(n, edges, succ_prob, start, end) == expected
