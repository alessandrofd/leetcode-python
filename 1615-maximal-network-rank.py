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
        adjs = defaultdict(list)
        for u, v in roads:
            adjs[u].append(v)
            adjs[v].append(u)

        max_rank = 0

        for u, v in combinations(range(n), 2):
            rank = len(adjs[u]) + len(adjs[v])
            if v in adjs[u]:
                rank -= 1
            max_rank = max(max_rank, rank)

        return max_rank

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjs = defaultdict(list)
        for u, v in roads:
            adjs[u].append(v)
            adjs[v].append(u)

        inbounds = sorted([(len(adjs[i]), i) for i in range(n)], reverse=True)
        most_connected = [inbounds[0], inbounds[1]]
        i = 2
        while i < len(inbounds) and inbounds[i][0] == inbounds[1][0]:
            most_connected.append(inbounds[i])
            i += 1

        max_rank = 0

        for i, j in combinations(range(len(most_connected)), 2):
            u, v = most_connected[i][1], most_connected[j][1]
            rank = len(adjs[u]) + len(adjs[v])
            if v in adjs[u]:
                rank -= 1
            if rank < max_rank:
                break
            max_rank = rank

        return max_rank


def test_solution():
    """test"""

    funcs = [
        Solution().maximalNetworkRank,
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
    result = Solution().maximalNetworkRank(4, [[0, 1], [0, 3], [1, 2], [1, 3]])
    print(result)
