"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""
from typing import List


class Solution:
    """solution class"""

    # Principal dificuldade é estabelecer a condição de saída do laço.
    def spiralOrder_loop(self, matrix: List[List[int]]) -> List[int]:
        """loop"""

    # Consome a matriz
    def spiralOrder_shift_reverse(self, matrix: List[List[int]]) -> List[int]:
        """shift/pop(0) and reverse"""


def test_solution():
    """test"""

    funcs = [
        Solution().spiralOrder_loop,
        Solution().spiralOrder_shift_reverse,
    ]

    data = [
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
            ],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
        (
            [
                [2, 5, 8],
                [4, 0, -1],
            ],
            [2, 5, 8, -1, 0, 4],
        ),
        ([[7], [9], [6]], [7, 9, 6]),
    ]

    for obstacles, expected in data:
        for func in funcs:
            assert func(obstacles) == expected
