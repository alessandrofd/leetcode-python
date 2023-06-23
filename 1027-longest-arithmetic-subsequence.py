"""
Given an array nums of integers, return the length of the longest arithmetic
subsequence in nums.

Note that:

    A subsequence is an array that can be derived from another array by
    deleting some or no elements without changing the order of the remaining
    elements.

    A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value
    (for 0 <= i < seq.length - 1).

Constraints:
    2 <= nums.length <= 1000
    0 <= nums[i] <= 500
"""


# DP com duas dimensões: posição no vetor e differença entre valores
# Caso base: dp[0][*] = 0
# Transição: dp[i][diff] = dp[j][diff] + 1, onde j < i e diff = nums[i] - nums[j]
# Resultado: max(dp[i][diff])

from typing import List
from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(lambda: 1) for _ in range(n)]
        max_length = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[j] - nums[i]
                dp[i][diff] = dp[j][diff] + 1
                max_length = max(max_length, dp[i][diff])
        return max_length


def test_solution():
    """test"""

    funcs = [
        Solution().longestArithSeqLength,
    ]

    # fmt: off
    data = [
        ([3, 6, 9, 12], 4),
        ([9, 4, 7, 2, 10], 3),
        ([20, 1, 15, 3, 10, 5, 8], 4),
    ]
    # fmt: on
    for nums, expected in data:
        for func in funcs:
            assert func(nums) == expected
