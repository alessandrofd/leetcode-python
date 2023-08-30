"""
You are given a 0-indexed integer array nums. In one operation you can
replace any element of the array with any two elements that sum to it.

    For example, consider nums = [5,6,7]. In one operation, we can replace
    nums[1] with 2 and 4 and convert nums to [5,2,4,7].

Return the minimum number of operations to make an array that is sorted in
non-decreasing order.

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
"""

from typing import List
from math import ceil


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        return -1


def test_solution():
    """test"""

    funcs = [Solution().minimumReplacement]

    # fmt: off
    data = [
        [[3, 9, 3], 2],
        [[1, 2, 3, 4, 5], 0],
        [[12, 9, 7, 6, 17, 19, 21], 6],
        [[7, 6, 15, 6, 11, 14, 10], 10],
    ]
    # fmt: on

    for nums, expected in data:
        for func in funcs:
            assert func(nums) == expected


if __name__ == "__main__":
    pass
