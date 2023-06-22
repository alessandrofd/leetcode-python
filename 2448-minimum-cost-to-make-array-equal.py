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
        n = len(nums)
        nums_and_cost = sorted([n, c] for n, c in zip(nums, cost))
        prefix_sum = list(accumulate(c for n, c in nums_and_cost))

        total_cost = 0
        for i in range(1, n):
            diff = nums_and_cost[i][0] - nums_and_cost[0][0]
            total_cost += diff * nums_and_cost[i][1]

        result = total_cost
        for i in range(1, n):
            diff = nums_and_cost[i][0] - nums_and_cost[i - 1][0]
            total_cost += prefix_sum[i - 1] * diff
            total_cost -= (prefix_sum[n - 1] - prefix_sum[i - 1]) * diff
            result = min(result, total_cost)

        return result

    def minCost_bin_search(self, nums: List[int], cost: List[int]) -> int:
        def get_cost(base: int) -> int:
            result = 0
            for n, c in zip(nums, cost):
                result += abs(n - base) * c
            return result

        lo = min(nums)
        hi = max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if get_cost(mid) > get_cost(mid + 1):
                lo = mid + 1
            else:
                hi = mid

        return get_cost(lo)

    def minCost_weighted_median(self, nums: List[int], cost: List[int]) -> int:
        nums_and_cost = sorted(zip(nums, cost))
        median_cost = sum(cost) // 2
        acc_cost = 0
        for n, c in nums_and_cost:
            acc_cost += c
            if acc_cost > median_cost:
                base = n
                return sum(c * abs(n - base) for n, c in nums_and_cost)


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
