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


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        return 0


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
