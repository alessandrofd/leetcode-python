"""
You are given two 0-indexed arrays nums and cost consisting each of n
positive integers.

You can do the following operation any number of times:

    Increase or decrease any element of the array nums by 1.

The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums
become equal.

Constraints:
    n == nums.length == cost.length
    1 <= n <= 10^5
    1 <= nums[i], cost[i] <= 10^6
"""
from typing import List
from itertools import accumulate


class Solution:
    def minCost_prefix_sum(self, nums: List[int], cost: List[int]) -> int:
        return 0

    def minCost_bin_search(self, nums: List[int], cost: List[int]) -> int:
        return 0

    def minCost_weighted_median(self, nums: List[int], cost: List[int]) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().minCost_prefix_sum,
        Solution().minCost_bin_search,
        Solution().minCost_weighted_median,
    ]

    # fmt: off
    data = [
        ([1, 3, 5, 2], [2, 3, 1, 14], 8),
        ([2, 2, 2, 2, 2], [4, 2, 8, 1, 3], 0),
    ]
    # fmt: on
    for nums, cost, expected in data:
        for func in funcs:
            assert func(nums, cost) == expected
