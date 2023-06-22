"""
You are given a positive integer n representing n cities numbered from 1 to n.
You are also given a 2D array roads where roads[i] = [ai, bi, distancei]
indicates that there is a bidirectional road between cities ai and bi with
a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of
a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

    A path is a sequence of roads between two cities.

    It is allowed for a path to contain the same road multiple times, and
    you can visit cities 1 and n multiple times along the path.

    The test cases are generated such that there is at least one path
    between 1 and n.

Constraints:
    2 <= n <= 10^5
    1 <= roads.length <= 10^5
    roads[i].length == 3
    1 <= ai, bi <= n
    ai != bi
    1 <= distancei <= 10^4
    There are no repeated edges.
    There is at least one path between 1 and n.
"""

from typing import List


class Solution:
    """Solution class"""

    def minScore(self, num_cities: int, roads: List[List[int]]) -> int:
        """Soluction func"""


def test_solution():
    """test"""

    funcs = [Solution().minScore]

    data = [
        (
            4,
            [
                [1, 2, 9],
                [2, 3, 6],
                [2, 4, 5],
                [1, 4, 7],
            ],
            5,
        ),
        (
            4,
            [
                [1, 2, 2],
                [1, 3, 4],
                [3, 4, 7],
            ],
            2,
        ),
    ]

    for num_cities, roads, output in data:
        for func in funcs:
            assert func(num_cities, roads) == output
