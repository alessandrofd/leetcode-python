"""
1675. Minimize Deviation in Array

You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number 
of times:

    If the element is even, divide it by 2.
        For example, if the array is [1,2,3,4], then you can do this operation 
        on the last element, and the array will be [1,2,3,2].

    If the element is odd, multiply it by 2.
        For example, if the array is [1,2,3,4], then you can do this operation 
        on the first element, and the array will be [2,2,3,4].

The deviation of the array is the maximum difference between any two elements in 
the array.

Return the minimum deviation the array can have after performing some number of 
operations.


Constraints:
    n == nums.length
    2 <= n <= 5 * 10^4
    1 <= nums[i] <= 10^9
"""

from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pass


nums = [1, 2, 3, 4]
# Output: 1
# Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2],
# then the deviation will be 3 - 2 = 1.

print(Solution().minimumDeviation(nums))

nums = [4, 1, 5, 20, 3]
# Output: 3
# Explanation: You can transform the array after two operations to [4,2,5,5,3],
# then the deviation will be 5 - 2 = 3.

print(Solution().minimumDeviation(nums))

nums = [2, 10, 8]
# Output: 3

print(Solution().minimumDeviation(nums))

nums = [3, 5]
# Output: 1

print(Solution().minimumDeviation(nums))
