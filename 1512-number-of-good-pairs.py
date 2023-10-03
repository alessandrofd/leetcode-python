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
        freqs = Counter(nums)

        good_pairs = 0
        for freq in freqs.values():
            good_pairs += freq * (freq - 1) // 2

        return good_pairs


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
