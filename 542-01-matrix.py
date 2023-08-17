"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for
each cell.

The distance between two adjacent cells is 1.

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 10^4
    1 <= m * n <= 10^4
    mat[i][j] is either 0 or 1.
    There is at least one 0 in mat.
"""

from typing import List
from collections import deque
from itertools import product


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        result = [[-1] * cols for _ in range(rows)]

        queue = deque()

        for row, col in product(range(rows), range(cols)):
            if matrix[row][col] == 0:
                result[row][col] = 0
                queue.append((row, col))

        deltas = ((-1, 0), (0, 1), (1, 0), (0, -1))

        def valid(row, col):
            if 0 <= row < rows and 0 <= col < cols and result[row][col] == -1:
                return True
            return False

        while queue:
            n = len(queue)
            for i in range(n):
                row, col = queue.popleft()
                for delta_row, delta_col in deltas:
                    next_row, next_col = row + delta_row, col + delta_col
                    if valid(next_row, next_col):
                        result[next_row][next_col] = result[row][col] + 1
                        queue.append((next_row, next_col))

        return result


def test_solution():
    """test"""

    funcs = [
        Solution().updateMatrix,
    ]

    # fmt: off
    data = [
        ([[0,0,0],[0,1,0],[0,0,0]], [[0,0,0],[0,1,0],[0,0,0]]), 
        ([[0,0,0],[0,1,0],[1,1,1]], [[0,0,0],[0,1,0],[1,2,1]]), 
    ]
    # fmt: on
    for mat, expected in data:
        for func in funcs:
            assert func(mat) == expected


if __name__ == "__main__":
    pass
