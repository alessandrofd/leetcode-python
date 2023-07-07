"""
Given an n x n binary matrix grid, return the length of the shortest clear
path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell
(i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.

    All the adjacent cells of the path are 8-directionally connected
    (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Constraints:
    n == grid.length
    n == grid[i].length
    1 <= n <= 100
    grid[i][j] is 0 or 1
"""

from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        moves = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        if grid[0][0] or grid[-1][-1]:
            return -1

        queue = deque([(0, 0, 1)])

        while queue:
            row, col, distance = queue.popleft()

            if row == n - 1 and col == n - 1:
                return distance

            if 0 <= row < n and 0 <= col < n and grid[row][col] == 0:
                grid[row][col] = 1
                for move_row, move_col in moves:
                    queue.append((row + move_row, col + move_col, distance + 1))
        return -1


def test_solution():
    """test"""

    funcs = [
        Solution().shortestPathBinaryMatrix,
    ]

    # fmt: off
    data = [
        ([ [0, 1], [1, 0], ], 2), 
        ([ [0, 0, 0], [1, 1, 0], [1, 1, 0], ], 4), 
        ([ [1, 0, 0], [1, 1, 0], [1, 1, 0], ], -1), 
    ]
    # fmt: on

    for grid, expected in data:
        for func in funcs:
            assert func(grid) == expected
