"""
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the
following conditions:

    The minimum value in the subarray is equal to minK.

    The maximum value in the subarray is equal to maxK.

Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

Constraints:
2 <= nums.length <= 10^5
1 <= nums[i], minK, maxK <= 10^6
"""
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        pass


data = [
    ([1, 3, 5, 2, 7, 5], 1, 5, 2),
    ([1, 1, 1, 1], 1, 1, 10),
]

funcs = [Solution().countSubarrays]

for nums, minK, maxK, output in data:
    print(f"nums = {nums}, minK = {minK}, maxK = {maxK}, Output = {output}")
    for func in funcs:
        print(f"{func.__name__} = {func(nums, minK, maxK)}")
