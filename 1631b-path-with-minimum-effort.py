"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D
array of size rows x columns, where heights[row][col] represents the height
of cell (row, col). You are situated in the top-left cell, (0, 0), and you
hope to travel to the bottom-right cell, (rows-1, columns-1)
(i.e., 0-indexed). You can move up, down, left, or right, and you wish to
find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two
consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the
bottom-right cell.

Constraints:
    rows == heights.length
    columns == heights[i].length
    1 <= rows, columns <= 100
    1 <= heights[i][j] <= 10^6
"""

from typing import List


class Solution:
    def minimumEffortPath_backtrack(self, heights: List[List[int]]) -> int:
        """Backtrack"""
        return -1

    def minimumEffortPath_dijkstra(self, heights: List[List[int]]) -> int:
        """Dijkstra"""
        return -1


def test_solution():
    """test"""

    funcs = [
        Solution().minimumEffortPath_backtrack,
        Solution().minimumEffortPath_dijkstra,
    ]

    # fmt: off
    data = [
        [[[1,2,2],[3,8,2],[5,3,5]], 2],
        [[[1,2,3],[3,8,4],[5,3,5]], 1],
        [[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]], 0],
    ]
    # fmt: on

    for heights, expected in data:
        for func in funcs:
            assert func(heights) == expected


if __name__ == "__main__":
    pass
