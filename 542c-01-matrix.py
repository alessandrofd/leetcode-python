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
        return [[0]]


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
