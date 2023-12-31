"""
There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost]
represents the cost to connect city1 and city2 together. A connection is
bidirectional: connecting city1 and city2 is the same as connecting city2 and
city1.

Return the minimum cost so that for every pair of cities, there exists a path
of connections (possibly of length 1) that connects those two cities together.
The cost is the sum of the connection costs used. If the task is impossible,
return -1.

Constraints:
    1 <= N <= 10000
    1 <= connections.length <= 10000
    1 <= connections[i][0], connections[i][1] <= N
    0 <= connections[i][2] <= 10^5
    connections[i][0] != connections[i][1]
"""

from typing import List


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        return -1


def test_solution():
    """test"""

    funcs = [
        Solution().minimumCost,
    ]

    data = [
        (
            3,
            [
                [1, 2, 5],
                [1, 3, 6],
                [2, 3, 1],
            ],
            6,
        ),
        (
            4,
            [
                [1, 2, 3],
                [3, 4, 4],
            ],
            -1,
        ),
    ]
    for n, connections, expected in data:
        for func in funcs:
            assert func(n, connections) == expected


if __name__ == "__main__":
    pass
