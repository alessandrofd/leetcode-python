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
        """solution method"""

        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        row, col = 0, 0
        count = 1

        while count < n * n:
            while col < right:
                matrix[row][col] = count
                col += 1
                count += 1
            top += 1

            while row < bottom:
                matrix[row][col] = count
                row += 1
                count += 1
            right -= 1

            while col > left:
                matrix[row][col] = count
                col -= 1
                count += 1
            bottom -= 1

            while row > top:
                matrix[row][col] = count
                row -= 1
                count += 1
            left += 1

        matrix[row][col] = count
        return matrix


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
