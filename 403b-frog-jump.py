"""
A frog is crossing a river. The river is divided into some number of units,
and at each unit, there may or may not exist a stone. The frog can jump on a
stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order,
determine if the frog can cross the river by landing on the last stone.
Initially, the frog is on the first stone and assumes the first jump must be
1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k,
or k + 1 units. The frog can only jump in the forward direction.

Constraints:
    2 <= stones.length <= 2000
    0 <= stones[i] <= 2^31 - 1
    stones[0] == 0
    stones is sorted in a strictly increasing order.
"""

from typing import List
from functools import cache
from bisect import bisect_left
from collections import defaultdict


class Solution:
    def canCross_dp_top_down(self, stones: List[int]) -> bool:
        """
        DP Top-Down
        """
        return False

    def canCross_dp_bottom_up(self, stones: List[int]) -> bool:
        """
        DP Bottom-Up
        """
        return False

    def canCross_bfs(self, stones: List[int]) -> bool:
        """
        BFS
        """
        return False


def test_solution():
    """test"""

    funcs = [
        Solution().canCross_dp_top_down,
        Solution().canCross_dp_bottom_up,
        Solution().canCross_bfs,
    ]

    # fmt: off
    data = [
        [[0, 1, 3, 5, 6, 8, 12, 17], True],
        [[0, 1, 2, 3, 4, 8, 9, 11], False],
        [[0, 1, 2147483647], False],
        [[0, 1, 3, 6, 10, 13, 15, 18], True]
    ]
    # fmt: on

    for stones, expected in data:
        for func in funcs:
            assert func(stones) == expected


if __name__ == "__main__":
    pass
