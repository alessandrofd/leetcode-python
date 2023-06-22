"""
Given an array of integers nums, sort the array in ascending order and
return it.

You must solve the problem without using any built-in functions in O(nlog(n))
time complexity and with the smallest space complexity possible.

Constraints:
    1 <= nums.length <= 5 * 10^4
    -5 * 10^4 <= nums[i] <= 5 * 10^4
"""


class Solution:
    """Solution class"""

    def sortArray_merge(self, nums):  # pylint: disable=invalid-name
        """Merge sort"""

    def sortArray_heap(self, nums):  # pylint: disable=invalid-name
        """Heap sort"""

    def sortArray_counting(self, nums):  # pylint: disable=invalid-name
        """Counting sort"""

    def sortArray_radix(self, nums):  # pylint: disable=invalid-name
        """Radix sort"""


data = [[5, 2, 3, 1], [5, 1, 1, 2, 0, 0, -11, -4, -25]]
# Output: [1,2,3,5]
# Output: [0,0,1,1,2,5]

funcs = [
    Solution().sortArray_merge,
    Solution().sortArray_heap,
    Solution().sortArray_counting,
    Solution().sortArray_radix,
]

for nums in data:
    for func in funcs:
        print(func(nums))
