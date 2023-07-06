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
        n = len(nums)
        MAX_LEN = int(1e5 + 1)
        min_len = MAX_LEN
        win_sum = 0
        start = 0

        for i, num in enumerate(nums):
            win_sum += num
            while win_sum >= target:
                min_len = min(min_len, i - start + 1)
                win_sum -= nums[start]
                start += 1

        return min_len if min_len < MAX_LEN else 0


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
