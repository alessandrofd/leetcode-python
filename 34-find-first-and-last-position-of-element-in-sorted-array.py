"""
Given an array of integers nums sorted in non-decreasing order, find the
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Constraints:
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    nums is a non-decreasing array.
    -10^9 <= target <= 10^9
"""

from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = bisect_left(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = bisect_right(nums, target) - 1

        return [start, end]


def test_solution():
    """test"""

    funcs = [
        Solution().searchRange,
    ]

    # fmt: off
    data = [
        [[5, 7, 7, 8, 8, 10], 8, [3, 4]],
        [[5, 7, 7, 8, 8, 10], 6, [-1, -1]],
        [[], 0, [-1, -1]],
    ]
    # fmt: on
    for nums, target, expected in data:
        for func in funcs:
            assert func(nums, target) == expected
