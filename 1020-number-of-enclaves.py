"""
You are given an m x n binary matrix grid, where 0 represents a sea cell
and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent
(4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the
boundary of the grid in any number of moves.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 500
    grid[i][j] is either 0 or 1.
"""

# Problema parecido ao 1254 - Number of closed islands. Vamos aplicar DSU na
# matriz linearizada. Percorreremos a matriz uma primeira vez em que
# agruparemos as células válidas outras células válida para trás, acima e
# à esquerda. Em seguida percorremos as células das bordas da matriz e
# acrescentamos os grupos às quais as células válidas pertencem, temos que
# resolver o encadeamento de parentes para isso, a um conjunto. Em seguida,
# percorremos o miolo da matriz contanto todas as células que não pertencem
# aos grupos da borda.

from itertools import product, chain


class Solution:
    def numEnclaves_dsu(self, grid):
        pass

    # Podemos aplicar DFS ao partir das bordas e visitando todas as células
    # conectadas, marcando-as como inválidas. A seguir percorremos o miolo da
    # matriz e contamos as células válidas.

    def numEnclaves_dfs(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(row, col):
            if (
                0 <= row < rows
                and 0 <= col < cols
                and not visited[row][col]
                and grid[row][col] == 1
            ):
                visited[row][col] = True
                dfs(row - 1, col)
                dfs(row, col - 1)
                dfs(row, col + 1)
                dfs(row + 1, col)

        for row, col in chain(
            product([0, rows - 1], range(cols)), product(range(rows), [0, cols - 1])
        ):
            dfs(row, col)

        middle = [
            grid[row][col]
            for row, col in product(range(1, rows - 1), range(1, cols - 1))
            if not visited[row][col]
        ]

        return sum(middle)

    # Quanto utilizamos BFS temos que ter o cuidado de marcar a célula como
    # visitada o quanto antes para evitar um enfileiramentos duplicados. Portanto,
    # temos que marcar a célula quando ele é enfileirada, evitando novos
    # enfileiramentos da mesma célula, e não no seu desfileiramento.

    def numEnclaves_bfs(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def bfs(row, col):
            visited[row][col] = True
            queue = [(row, col)]

            while queue:
                row, col = queue.pop(0)
                for d_row, d_col in chain(product([-1, 1], [0]), product([0], [-1, 1])):
                    new_row, new_col = row + d_row, col + d_col
                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and not visited[new_row][new_col]
                        and grid[new_row][new_col] == 1
                    ):
                        visited[new_row][new_col] = True
                        queue.append((new_row, new_col))

        for row, col in chain(
            product([0, rows - 1], range(cols)), product(range(rows), [0, cols - 1])
        ):
            if grid[row][col] == 1:
                bfs(row, col)

        middle = [
            grid[row][col]
            for row, col in product(range(1, rows - 1), range(1, cols - 1))
            if not visited[row][col]
        ]

        return sum(middle)


def test_solution():
    """test"""

    funcs = [
        # Solution().numEnclaves_dsu,
        Solution().numEnclaves_dfs,
        Solution().numEnclaves_bfs,
    ]

    data = [
        (
            [
                [0, 0, 0, 0],
                [1, 0, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
            ],
            3,
        ),
        (
            [
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0],
            ],
            0,
        ),
    ]

    for grid, output in data:
        for func in funcs:
            assert func(grid) == output
