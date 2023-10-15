"""
You have a pointer at index 0 in an array of size arrLen. At each step, you
can move 1 position to the left, 1 position to the right in the array, or
stay in the same place (The pointer should not be placed outside the array at
any time).

Given two integers steps and arrLen, return the number of ways such that your
pointer is still at index 0 after exactly steps steps. Since the answer may
be too large, return it modulo 10^9 + 7.

Constraints:
    1 <= steps <= 500
    1 <= arrLen <= 10^6
"""

from functools import cache


class Solution:
    def numWays_top_down(self, steps: int, arrLen: int) -> int:
        # Notice in the constraints that while steps can be up to 500, arrLen
        # can be up to 10^6. However, it is impossible for any call to have a
        # value of i greater than steps. The furthest we can go is by only
        # making moves to the right, but we would run out of moves after steps
        # moves. Thus, we can safely perform arrLen = min(arrLen, steps) before
        # starting the algorithm.

        return -1

    def numWays_bottom_up(self, steps: int, arr_len: int) -> int:
        return -1

    def numWays_bottom_up_space_optimized(self, steps: int, arr_len: int) -> int:
        return -1


def test_solution():
    """test"""

    funcs = [
        Solution().numWays_top_down,
        Solution().numWays_bottom_up,
        Solution().numWays_bottom_up_space_optimized,
    ]

    # fmt: off
    data = [
        [3, 2, 4],
        [2, 4, 2],
        [4, 2, 8],
    ]
    # fmt: on
    for func in funcs:
        for steps, arr_len, expected in data:
            assert func(steps, arr_len) == expected
