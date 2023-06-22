"""
Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.
"""

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [n for n, _ in Counter(nums).most_common(k)]


def test_solution():
    """test"""

    funcs = [
        Solution().topKFrequent,
    ]

    data = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
    ]

    for nums, k, expected in data:
        for func in funcs:
            assert func(nums, k) == expected
