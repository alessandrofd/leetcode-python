"""
There are n cities. Some of them are connected, while some are not. If city a
is connected directly with city b, and city b is connected directly with
city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other
cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if
the ith city and the jth city are directly connected, and
isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Constraints:
    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] is 1 or 0.
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]
"""

# DSU

from typing import List


class Solution:
    def findCircleNum(self, connections: List[List[int]]) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().findCircleNum,
    ]

    # fmt: off
    data = [
        ([[1,1,0],[1,1,0],[0,0,1]], 2),
        ([[1,0,0],[0,1,0],[0,0,1]], 3),
    ]
    # fmt: on

    for connections, expected in data:
        for func in funcs:
            assert func(connections) == expected
