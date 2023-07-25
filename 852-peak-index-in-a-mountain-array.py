"""
An array arr a mountain if the following properties hold:

    arr.length >= 3

    There exists some i with 0 < i < arr.length - 1 such that:

        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]

        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given a mountain array arr, return the index i such that
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

Constraints:
    3 <= arr.length <= 10^5
    0 <= arr[i] <= 10^6
    arr is guaranteed to be a mountain array.
"""

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid - 1] < arr[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1


def test_solution():
    """test"""

    funcs = [
        Solution().peakIndexInMountainArray,
    ]

    # fmt: off
    data = [
        ([0, 1, 0], 1),
        ([0, 2, 1, 0], 1),
        ([0, 10, 5, 2], 1),
    ]
    # fmt: on
    for arr, expected in data:
        for func in funcs:
            assert func(arr) == expected
