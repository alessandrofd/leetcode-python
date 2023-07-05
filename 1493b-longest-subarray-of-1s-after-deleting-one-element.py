"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in 
the resulting array. Return 0 if there is no such subarray.

Constraints:
    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        return -1


def test_solution():
    """test"""

    funcs = [
        Solution().longestSubarray,
    ]

    # fmt: off
    data = [
        ([1,1,0,1], 3),
        ([0,1,1,1,0,1,1,0,1], 5),
        ([1,1,1], 2),
    ]
    # fmt: on
    for nums, expected in data:
        for func in funcs:
            assert func(nums) == expected
