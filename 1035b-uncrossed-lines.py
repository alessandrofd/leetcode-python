"""
You are given two integer arrays nums1 and nums2. We write the integers of
nums1 and nums2 (in the order they are given) on two separate horizontal
lines.

We may draw connecting lines: a straight line connecting two numbers
nums1[i] and nums2[j] such that:

    nums1[i] == nums2[j], and

    the line we draw does not intersect any other connecting (non-horizontal)
    line.

Note that a connecting line cannot intersect even at the endpoints
(i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.

Constraints:
    1 <= nums1.length, nums2.length <= 500
    1 <= nums1[i], nums2[j] <= 2000
"""


# Programação dinâmica - 2 dimensões: a quantidade de números em cada vetor
# consideradas
# Caso base: dp[0][j] = dp[i][0] = 0
# Transiçaõ :   
#   se nums1[i-1] == nums2[j-1] => dp[i][j] = 1 + dp[i-1][j-1]
#   senão dp[i][j] = max(dp[i][j-1], dp[i-1][j])
# Solução: dp[n1, n2], onde n1 = nums1.length e n2 = nums2.length

from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        pass

def test_solution():
    """test"""

    funcs = [
        Solution().maxUncrossedLines,
    ]

    data = [
        ([1, 4, 2], [1, 2, 4], 2),
        ([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2], 3),
        ([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1], 2),
    ]

    for nums1, nums2, expected in data:
        for func in funcs:
            assert func(nums1, nums2) == expected
