"""
You are given an n x n binary matrix grid where 1 represents land and 0
represents water.

An island is a 4-directionally connected group of 1's not connected to any
other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

Constraints:
    n == grid.length == grid[i].length
    2 <= n <= 100
    grid[i][j] is either 0 or 1.
    There are exactly two islands in grid.
"""

# O primeiro passo é identificar uma das ilhas e enfileirar todas as células
# que a compõem. Para tanto, podemos utilizar DFS. Em seguida, desenfileiramos
# todos os nós e exploramos os nós adjacentes. Os nós que representarem água são
# adicionados a uma nova fila. Quando a fila original for toda consumida,
# incrementamos a distância percorrida e trocamos a fila vazia pela nova fila.
# Assim que atingirmos o outra ilha, retornamos a distância. Este segundo
# procedimento descreve BFS.

from typing import List
from itertools import product


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # start_row, start_col = 0, 0
        # for start_row in range(n):
        #     for start_col in range(n):
        #         if grid[start_row][start_col] == 1:
        #             break
        #     else:
        #         continue
        #     break

        for start_row, start_col in product(range(n), range(n)):
            if grid[start_row][start_col] == 1:
                break

        queue = []

        deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def mark_island(row, col):
            if not (0 <= row < n and 0 <= col < n):
                return
            if grid[row][col] != 1:
                return

            grid[row][col] = 2
            queue.append((row, col))

            for delta_row, delta_col in deltas:
                mark_island(row + delta_row, col + delta_col)

        mark_island(start_row, start_col)

        distance = 0

        while queue:
            new_queue = []
            for row, col in queue:
                for delta_row, delta_col in deltas:
                    new_row = row + delta_row
                    new_col = col + delta_col
                    if not (0 <= new_row < n and 0 <= new_col < n):
                        continue

                    if grid[new_row][new_col] == 1:
                        return distance

                    if grid[new_row][new_col] != 0:
                        continue

                    grid[new_row][new_col] = -1
                    new_queue.append((new_row, new_col))

            distance += 1
            queue = new_queue


def test_solution():
    """test"""

    funcs = [
        Solution().shortestBridge,
    ]

    data = [
        (
            [
                [0, 1],
                [1, 0],
            ],
            1,
        ),
        (
            [
                [0, 1, 0],
                [0, 0, 0],
                [0, 0, 1],
            ],
            2,
        ),
        (
            [
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
            ],
            1,
        ),
    ]

    for grid, expected in data:
        for func in funcs:
            assert func(grid) == expected
