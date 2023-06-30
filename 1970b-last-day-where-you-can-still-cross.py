"""
There is a 1-based binary matrix where 0 represents land and 1 represents
water. You are given integers row and col representing the number of rows and
columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell
becomes flooded with water. You are given a 1-based 2D array cells, where
cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row
and cith column (1-based coordinates) will be covered with water
(i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to
the bottom by only walking on land cells. You can start from any cell in
the top row and end at any cell in the bottom row. You can only travel in
the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom
by only walking on land cells.

Constraints:
    2 <= row, col <= 2 * 10^4
    4 <= row * col <= 2 * 10^4
    cells.length == row * col
    1 <= ri <= row
    1 <= ci <= col
    All the values of cells are unique.
"""

from typing import List


class Solution:
    def latestDayToCross(self, rows: int, cols: int, cells: List[List[int]]) -> int:
        """DSU com grid"""

        return -1


def test_solution():
    """test"""

    funcs = [
        Solution().latestDayToCross,
    ]

    # fmt: off
    data = [
        # (2, 2, [ [1, 1], [2, 1], [1, 2], [2, 2], ], 2),
        # (2, 2, [ [1, 1], [1, 2], [2, 1], [2, 2], ], 1),
        # (3, 3, [ [1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1], ], 3),
        (6, 2, [ [4, 2], [6, 2], [2, 1], [4, 1], [6, 1], [3, 1], [2, 2], [3, 2], [1, 1], [5, 1], [5, 2], [1, 2] ], 3),
    ]
    # fmt: on
    for row, col, cells, expected in data:
        for func in funcs:
            assert func(row, col, cells) == expected
