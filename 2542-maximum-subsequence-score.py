"""
You are given two 0-indexed integer arrays nums1 and nums2 of equal length n
and a positive integer k. You must choose a subsequence of indices from nums1
of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

    The sum of the selected elements from nums1 multiplied with the minimum of
    the selected elements from nums2.

    It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) *
    min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).

Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from
the set {0, 1, ..., n-1} by deleting some or no elements.

Constraints:
    n == nums1.length == nums2.length
    1 <= n <= 10^5
    0 <= nums1[i], nums2[j] <= 10^5
    1 <= k <= n
"""


# A conversão do priority queue para array é muito cara. Melhor manter a soma
# dos maiores k - 1 valores do vetor nums1 à medida em que são enfileirados

from typing import List
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        merged = sorted(zip(nums1, nums2), key=lambda nums: nums[1], reverse=True)

        heap = [merged[i][0] for i in range(k - 1)]
        heapq.heapify(heap)

        max_sum = sum(heap)

        score = 0
        for i in range(k - 1, len(merged)):
            max_sum += merged[i][0]
            score = max(score, max_sum * merged[i][1])

            heapq.heappush(heap, merged[i][0])
            max_sum -= heapq.heappop(heap)

        return score


def test_solution():
    """test"""

    funcs = [
        Solution().maxScore,
    ]

    data = [
        ([1, 3, 3, 2], [2, 1, 3, 4], 3, 12),
        ([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1, 30),
    ]

    for nums1, nums2, k, expected in data:
        for func in funcs:
            assert func(nums1, nums2, k) == expected
