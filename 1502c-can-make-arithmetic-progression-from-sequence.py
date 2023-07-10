"""
A sequence of numbers is called an arithmetic progression if the difference 
between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to 
form an arithmetic progression. Otherwise, return false.

Constraints:
    2 <= arr.length <= 1000
    -10^6 <= arr[i] <= 10^6
"""


from typing import List
from itertools import pairwise


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        return False

    def canMakeArithmeticProgression_pairwise(self, arr: List[int]) -> bool:
        return False


def test_solution():
    """test"""

    funcs = [
        Solution().canMakeArithmeticProgression,
        Solution().canMakeArithmeticProgression_pairwise,
    ]

    # fmt: off
    data = [
        ([3, 5, 1], True),
        ([1, 2, 4], False),
    ]
    # fmt: on
    for arr, expected in data:
        for func in funcs:
            assert func(arr) == expected
