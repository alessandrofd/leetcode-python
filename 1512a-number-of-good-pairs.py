"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100
"""

from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().numIdenticalPairs,
    ]

    # fmt: off
    data = [
        [[1, 2, 3, 1, 1, 3], 4],
        [[1, 1, 1, 1], 6],
        [[1, 2, 3], 0],
    ]
    # fmt: on
    for nums, expected in data:
        for func in funcs:
            assert func(nums) == expected
