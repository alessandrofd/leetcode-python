"""
You are given an m x n integer matrix matrix with the following two
properties:

    Each row is sorted in non-decreasing order.

    The first integer of each row is greater than the last integer of the
    previous row.

Given an integer target, return true if target is in matrix or false
otherwise.

You must write a solution in O(log(m * n)) time complexity.

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -10^4 <= matrix[i][j], target <= 10^4
"""

from typing import List
from bisect import bisect_right


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return False


def test_solution():
    """test"""

    funcs = [
        Solution().searchMatrix,
    ]

    # fmt: off
    data = [
        ([ [1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], ], 3, True),
        ([ [1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60], ], 13, False),
        ([[1]], 1, True),
    ]
    # fmt: on
    for matrix, target, expected in data:
        for func in funcs:
            assert func(matrix, target) == expected


if __name__ == "__main__":
    pass
