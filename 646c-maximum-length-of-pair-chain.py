"""
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and
lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can
be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.

Constraints:
    n == pairs.length
    1 <= n <= 1000
    -1000 <= lefti < righti <= 1000
"""

from typing import List
from functools import cache


class Solution:
    def findLongestChain_dp_top_down(self, pairs: List[List[int]]) -> int:
        return 0

    def findLongestChain_dp_bottom_up(self, pairs: List[List[int]]) -> int:
        return 0

    def findLongestChain_greedy(self, pairs: List[List[int]]) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().findLongestChain_dp_top_down,
        Solution().findLongestChain_dp_bottom_up,
        Solution().findLongestChain_greedy,
    ]

    # fmt: off
    data = [
        [ [ [1, 2], [2, 3], [3, 4], ], 2, ],
        [ [ [1, 2], [7, 8], [4, 5], ], 3, ],
    ]
    # fmt: on

    for pairs, expected in data:
        for func in funcs:
            assert func(pairs) == expected


if __name__ == "__main__":
    result = Solution().findLongestChain_greedy(
        [
            [1, 2],
            [2, 3],
            [3, 4],
        ]
    )
    print(result)
