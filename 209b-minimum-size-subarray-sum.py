"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or equal to
target. If there is no such subarray, return 0 instead.

Constraints:
    1 <= target <= 10^9
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 104
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().minSubArrayLen,
    ]

    data = [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
    ]
    for target, nums, expected in data:
        for func in funcs:
            assert func(target, nums) == expected
