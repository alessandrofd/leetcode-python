"""
Given an integer n, return an array ans of length n + 1 such that for each i
(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Constraints:
    0 <= n <= 10^5
"""

from typing import List


class Solution:
    def countBits_pattern(self, n: int) -> List[int]:
        return [0]

    def countBits_shift(self, n: int) -> List[int]:
        return [0]


def test_solution():
    """test"""

    funcs = [
        Solution().countBits_pattern,
        Solution().countBits_shift,
    ]

    data = [
        [2, [0, 1, 1]],
        [5, [0, 1, 1, 2, 1, 2]],
    ]

    for n, expected in data:
        for func in funcs:
            assert func(n) == expected
