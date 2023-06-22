"""
Given a m x n grid filled with non-negative numbers, find a path from top
left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 100
"""

from typing import List

# Podemos reduzir a matriz a um grafo e percorrer o grafo da esquerda para
# direita e de cima para baixo até atingir o seu ponto final. Como o próprio
# enunciado do problema estabelece, podemos nos mover na matriz em um único
# sentido - isto torna o grafo resultante dirigido e, neste caso, dada a
# estrutura da matriz, acíclico.
#
# A melhor estratégia para percorrer o grafo é o BFS, pois garantirá que todos
# os caminhos que antecedem um nó já tenham sido percorridos ao analisá-lo.
# Mas como há mais de um caminho que leva a um nó, podemos controlar se este
# já está na fila de processamento.


class Solution:
    def minPathSum_bfs(self, grid: List[List[int]]) -> int:
        return 0

    # Não precisamos da fila nem do vetor para controlar os nós já visitados.
    # Podemos simplesmente percorrer a matriz na direção permitida que os caminhos
    # que levam ao próximo nó já terão sido percorridos.

    def minPathSum_dp(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        sum_row = 0
        for row in range(rows):
            sum_row += grid[row][0]
            grid[row][0] = sum_row

        sum_col = 0
        for col in range(cols):
            sum_col += grid[0][col]
            grid[0][col] = sum_col

        for row in range(1, rows):
            for col in range(1, cols):
                shortest = min(grid[row - 1][col], grid[row][col - 1])
                grid[row][col] = shortest + grid[row][col]

        return grid[-1][-1]


def test_solution():
    """test"""

    funcs = [Solution().minPathSum_dp]

    data = [
        (
            [
                [1, 3, 1],
                [1, 5, 1],
                [4, 2, 1],
            ],
            7,
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
            ],
            12,
        ),
    ]

    for grid, output in data:
        for func in funcs:
            assert func(grid) == output
