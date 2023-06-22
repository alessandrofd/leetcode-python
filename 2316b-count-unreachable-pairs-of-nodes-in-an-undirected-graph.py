"""
You are given an integer n. There is an undirected graph with n nodes,
numbered from 0 to n - 1. You are given a 2D integer array edges where
edges[i] = [ai, bi] denotes that there exists an undirected edge connecting
nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from
each other.

Constraints:
    1 <= n <= 10^5
    0 <= edges.length <= 2 * 10^5
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    There are no repeated edges.
"""

from typing import List


class Solution:
    """Solutin class"""

    def countPairs(self, num_nodes: int, edges: List[List[int]]) -> int:
        """Solution method"""


def test_solution():
    """test"""

    funcs = [Solution().countPairs]

    data = [
        (
            3,
            [
                [0, 1],
                [0, 2],
                [1, 2],
            ],
            0,
        ),
        (
            7,
            [
                [0, 2],
                [0, 5],
                [2, 4],
                [1, 6],
                [5, 4],
            ],
            14,
        ),
        (
            11,
            [
                [5, 0],
                [1, 0],
                [10, 7],
                [9, 8],
                [7, 2],
                [1, 3],
                [0, 2],
                [8, 5],
                [4, 6],
                [4, 2],
            ],
            0,
        ),
        (
            5,
            [
                [0, 3],
                [4, 1],
                [0, 1],
            ],
            4,
        ),
    ]

    for num_nodes, edges, output in data:
        for func in funcs:
            assert func(num_nodes, edges) == output
