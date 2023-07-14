"""
Given an integer array arr and an integer difference, return the length of
the longest subsequence in arr which is an arithmetic sequence such that
the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or
no elements without changing the order of the remaining elements.

Constraints:
    1 <= arr.length <= 10^5
    -10^4 <= arr[i], difference <= 10^4
"""

# Programação dinâmica
# Dimensão: elemento avaliado
# Transição: dp[arr[i]] = dp[arr[i] - difference] + 1
# Condição inicial: dp[arr[0]] = 1
# Resultado: max(dp[arr[i]])


from typing import List
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().longestSubsequence,
    ]

    # fmt: off
    data = [
        ([1, 2, 3, 4], 1, 4), 
        ([1, 3, 5, 7], 1, 1), 
        ([1, 5, 7, 8, 5, 3, 4, 2, 1], -2, 4), 
    ]
    # fmt: on
    for num_courses, prerequisites, expected in data:
        for func in funcs:
            assert func(num_courses, prerequisites) == expected
