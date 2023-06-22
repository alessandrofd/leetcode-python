"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 
to n^2 in spiral order.

Constraints:
    1 <= n <= 20
"""

from typing import List


class Solution:
    """solution class"""

    def generateMatrix(self, n: int) -> List[List[int]]:


def test_solution():
    """test"""

    funcs = [
        Solution().generateMatrix,
    ]

    data = [
        (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
        (1, [[1]]),
    ]

    for n, expected in data:
        for func in funcs:
            assert func(n) == expected
