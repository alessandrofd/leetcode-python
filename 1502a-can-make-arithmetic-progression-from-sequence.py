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
        n = len(arr)
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, n):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True

    def canMakeArithmeticProgression_pairwise(self, arr: List[int]) -> bool:
        (x, y), *rest = pairwise(sorted(arr))
        return all(b - a == y - x for a, b in rest)


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
