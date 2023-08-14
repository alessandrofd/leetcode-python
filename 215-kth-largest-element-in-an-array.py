"""
Given an integer array nums and an integer k, return the kth largest element
in the array

Note that it is the kth largest element in the sorted order, not the kth
distinct element.

Can you solve it without sorting?

Constraints:
    1 <= k <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
"""

from typing import List
from heapq import heappush, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)

        return heap[0]


def test_solution():
    """test"""

    funcs = [
        Solution().findKthLargest,
    ]

    # fmt: off
    data = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ]
    # fmt: on
    for nums, k, expected in data:
        for func in funcs:
            assert func(nums, k) == expected


if __name__ == "__main__":
    pass
