"""
'You are given an array points representing integer coordinates of some points
on a 2D-plane, where points[i] = [xi, yi]

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan
distance between them: |xi - xj| + |yi - yj|, where |val| denotes the
absolute value of val.

Return the minimum cost to make all points connected. All points are
connected if there is exactly one simple path between any two points.

Constraints:
    1 <= points.length <= 1000
    -10^6 <= xi, yi <= 10^6
    All pairs (xi, yi) are distinct.
"""

from typing import List
from itertools import product


class Solution:
    def minCostConnectPoints_kruskal(self, points: List[List[int]]) -> int:
        return -1

    def minCostConnectPoints_prim(self, points: List[List[int]]) -> int:
        return -1

    def minCostConnectPoints_prim_cached(self, points: List[List[int]]) -> int:
        return -1


def test_solution():
    """test"""

    funcs = [
        Solution().minCostConnectPoints_kruskal,
        Solution().minCostConnectPoints_prim,
        Solution().minCostConnectPoints_prim_cached,
    ]

    data = [
        (
            [
                [0, 0],
                [2, 2],
                [3, 10],
                [5, 2],
                [7, 0],
            ],
            20,
        ),
        (
            [
                [3, 12],
                [-2, 5],
                [-4, 1],
            ],
            18,
        ),
        ([[-1000000, -1000000], [1000000, 1000000]], 4_000_000),
    ]
    for points, expected in data:
        for func in funcs:
            assert func(points) == expected


if __name__ == "__main__":
    pass
