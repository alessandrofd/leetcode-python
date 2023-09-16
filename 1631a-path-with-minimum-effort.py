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
from heapq import heappush, heappop


class Solution:
    def minimumEffortPath_backtrack(self, heights: List[List[int]]) -> int:
        """Backtrack - TLE"""

        rows = len(heights)
        cols = len(heights[0])

        min_effort = 1_000_000

        def backtrack(row: int, col: int, max_diff: int) -> None:
            nonlocal min_effort

            def is_valid_cell(r: int, c: int) -> bool:
                return 0 <= r < rows and 0 <= c < cols

            deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            if row == rows - 1 and col == cols - 1:
                min_effort = min(min_effort, max_diff)

            curr_height = heights[row][col]
            heights[row][col] = 0

            for delta_row, delta_col in deltas:
                adj_row, adj_col = row + delta_row, col + delta_col

                if (
                    not is_valid_cell(adj_row, adj_col)
                    or heights[adj_row][adj_col] == 0
                ):
                    continue

                curr_diff = abs(curr_height - heights[adj_row][adj_col])
                max_curr_diff = max(max_diff, curr_diff)
                if max_curr_diff < min_effort:
                    backtrack(adj_row, adj_col, max_curr_diff)

            heights[row][col] = curr_height

        backtrack(0, 0, 0)
        return min_effort

    def minimumEffortPath_dijkstra(self, heights: List[List[int]]) -> int:
        """Dijkstra"""
        rows = len(heights)
        cols = len(heights[0])

        def is_valid_cell(r: int, c: int) -> bool:
            return 0 <= r < rows and 0 <= c < cols

        deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        diffs = [[1_000_000] * cols for _ in range(rows)]
        visited = [[False] * cols for _ in range(rows)]

        diffs[0][0] = 0

        heap = []
        heappush(heap, (0, 0, 0))

        while heap:
            max_diff, row, col = heappop(heap)
            visited[row][col] = True

            for delta_row, delta_col in deltas:
                adj_row, adj_col = row + delta_row, col + delta_col

                if not is_valid_cell(adj_row, adj_col) or visited[adj_row][adj_col]:
                    continue

                curr_diff = abs(heights[row][col] - heights[adj_row][adj_col])
                max_curr_diff = max(max_diff, curr_diff)
                if diffs[adj_row][adj_col] > max_curr_diff:
                    diffs[adj_row][adj_col] = max_curr_diff
                    heappush(heap, (max_curr_diff, adj_row, adj_col))

        return diffs[rows - 1][cols - 1]


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
