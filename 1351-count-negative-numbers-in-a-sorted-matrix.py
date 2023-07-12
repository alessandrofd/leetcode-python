"""
Given a m x n matrix grid which is sorted in non-increasing order both
row-wise and column-wise, return the number of negative numbers in grid.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100
"""

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])

        last_positive = cols - 1
        count = 0

        for row in grid:
            lo = 0
            hi = last_positive
            while lo <= hi:
                mid = (lo + hi) // 2
                if row[mid] >= 0:
                    lo = mid + 1
                else:
                    hi = mid - 1
            last_positive = lo - 1
            count += cols - 1 - last_positive

        return count


def test_solution():
    """test"""

    funcs = [
        Solution().countNegatives,
    ]

    # fmt: off
    data = [
        ([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]], 8), 
        ([[3,2],[1,0]], 0), 
    ]
    # fmt: on
    for grid, expected in data:
        for func in funcs:
            assert func(grid) == expected
