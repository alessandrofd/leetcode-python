"""
Given two integer arrays arr1 and arr2, return the minimum number of
operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and
0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.

Constraints:
    1 <= arr1.length, arr2.length <= 2000
    0 <= arr1[i], arr2[i] <= 10^9
"""

from typing import List
from bisect import bisect_right
from functools import cache
from collections import defaultdict


class Solution:
    def makeArrayIncreasing_dp_top_down(self, arr1: List[int], arr2: List[int]) -> int:
        return 0

    def makeArrayIncreasing_dp_bottom_up(self, arr1: List[int], arr2: List[int]) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().makeArrayIncreasing_dp_top_down,
        Solution().makeArrayIncreasing_dp_bottom_up,
    ]

    # fmt: off
    data = [
        ([1, 5, 3, 6, 7], [1, 3, 2, 4], 1),
        ([1, 5, 3, 6, 7], [4, 3, 1], 2),
        ([1, 5, 3, 6, 7], [1, 6, 3, 3], -1),
        (
            [5, 16, 19, 2, 1, 12, 7, 14, 5, 16],
            [6, 17, 4, 3, 6, 13, 4, 3, 18, 17, 16, 7, 14, 1, 16],
            8
        ),
    ]
    # fmt: on
    for arr1, arr2, expected in data:
        for func in funcs:
            assert func(arr1, arr2) == expected
