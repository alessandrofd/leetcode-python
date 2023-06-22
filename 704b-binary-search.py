"""
# Given an array of integers nums which is sorted in ascending order, and
# an integer target, write a function to search target in nums. If target
# exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Constraints:
#    1 <= nums.length <= 10^4
#    -10^4 < nums[i], target < 10^4
#    All the integers in nums are unique.
#    nums is sorted in ascending order.
"""

import bisect


class Solution:
    def search_pointers(self, nums, target):

    def search_bisect(self, nums, target):


def test_solution():

    """test"""

    funcs = [Solution().search_pointers, Solution().search_bisect]

    data = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    ]

    for nums, target, output in data:
        for func in funcs:
            assert func(nums, target) == output
