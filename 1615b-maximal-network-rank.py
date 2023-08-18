"""
There is an infrastructure of n cities with some number of roads connecting
these cities. Each roads[i] = [ai, bi] indicates that there is a
bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of
directly connected roads to either city. If a road is directly connected to
both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of
all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of
the entire infrastructure.

Constraints:
    2 <= n <= 100
    0 <= roads.length <= n * (n - 1) / 2
    roads[i].length == 2
    0 <= ai, bi <= n-1
    ai != bi
    Each pair of cities has at most one road connecting them.
"""

from typing import List
from collections import defaultdict
from itertools import combinations


class Solution:
    def maximalNetworkRank_combination(self, n: int, roads: List[List[int]]) -> int:
        return 0

    def maximalNetworkRank_sort(self, n: int, roads: List[List[int]]) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().maximalNetworkRank_combination,
        Solution().maximalNetworkRank_sort,
    ]

    # fmt: off
    data = [
        (4, [ [0, 1], [0, 3], [1, 2], [1, 3], ], 4),
        (5, [ [0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4], ], 5),
        (8, [ [0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7], ], 5),
    ]
    # fmt: on
    for n, roads, expected in data:
        for func in funcs:
            assert func(n, roads) == expected


if __name__ == "__main__":
    # fmt: off
    result = Solution().maximalNetworkRank_sort(4, [[0, 1], [0, 3], [1, 2], [1, 3]])
    print(result)
