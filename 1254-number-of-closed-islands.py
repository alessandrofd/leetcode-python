"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal
4-directionally connected group of 0s and a closed island is an island
totally (all left, top, right, bottom) surrounded by 1s.]

Return the number of closed islands.

Constraints:
    1 <= grid.length, grid[0].length <= 100
    0 <= grid[i][j] <=1
"""

# Podemos aplicar DSU e partir do princípio que todas as células das primeiras
# e últimas linhas e colunas estão ligadas ao continentes. Agrupamos as demais
# células e a resposta será a quantidade de grupos - 1, este um correspondendo
# justamente às células ligadas ao continente. Precisamos linearizar a matriz,
# que é a aplicação de uma equação simples sem qualquer problemas. No entanto,
# mesmo após agruparmos todas as células, temos que revisitá-las para obter
# a verdadeira raiz do seu grupo, pois é possível que haja encadeamentos
# não resolvidos.


# Uma melhoria que podemos aplicar é agrupar as células da matriz apenas com
# as células que ficaram para trás, acima é à esquerda ao invés das quatro
# células que a rodeiam. O efeito é o mesmo, não considerando o ganho em
# processamento, pois a operação de agrupamento é transitiva. Neste caso, não
# podemos isolar as bordas como fizemos na solução anterior. Logo, é possível
# que as células ligadas ao continente pertençam a mais de um agrupamento.
# Temos que contar todos os grupos e subtrair deste total aqueles ligados ao
# continente, ao percorrer as células da borda.


# Uma última melhoria que podemos operar é ajustar a função de agrupamento
# - union(i, j) - para que ela retorne se houve um agrupamento ou não. Isto
# permite que subtraiamos do total de células de terra firma (os 0's)
# a quantidade de agrupamentos, o que resultará na quantidade final de grupos.
# Isto torna a segunda travessia da matriz restrita às células da borda
# da matriz. Esta travesia ainda é  necessária para descobrirmos a quantidade
# de grupos ligados ao continente, que será subtraído do valor total e
# produzirá o resultado final,


class Solution:
    def closedIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        parent = list(range(rows * cols))
        rank = [1] * (rows * cols)

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            i = find(i)
            j = find(j)

            if i == j:
                return False

            if rank[i] >= rank[j]:
                parent[j] = i
                rank[i] += rank[j]
            else:
                parent[i] = j
                rank[j] += rank[i]

            return True

        def flatten(row, col):
            return col + row * cols

        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    flat_index = flatten(row, col)
                    count += 1
                    if (
                        row > 0
                        and grid[row - 1][col] == 0
                        and union(flat_index, flatten(row - 1, col))
                    ):
                        count -= 1
                    if (
                        col > 0
                        and grid[row][col - 1] == 0
                        and union(flat_index, flatten(row, col - 1))
                    ):
                        count -= 1

        border_groups = set()
        for row in [0, rows - 1]:
            for col in range(cols):
                if grid[row][col] == 0:
                    border_groups.add(find(flatten(row, col)))

        for col in [0, cols - 1]:
            for row in range(rows):
                if grid[row][col] == 0:
                    border_groups.add(find(flatten(row, col)))

        return count - len(border_groups)


def test_solution():
    """test"""

    funcs = [Solution().closedIsland]

    data = [
        (
            [
                [1, 1, 1, 1, 1, 1, 1, 0],  # 0 - 7
                [1, 0, 0, 0, 0, 1, 1, 0],  # 8 - 15
                [1, 0, 1, 0, 1, 1, 1, 0],  # 16 - 23
                [1, 0, 0, 0, 0, 1, 0, 1],  # 24 - 31
                [1, 1, 1, 1, 1, 1, 1, 0],  # 32 - 39
            ],
            2,
        ),
        (
            [
                [0, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
            ],
            1,
        ),
        (
            [
                [1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],
            ],
            2,
        ),
        (
            [
                [0, 1, 1, 1, 0],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [0, 1, 1, 1, 0],
            ],
            1,
        ),
        (
            [
                [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],  # 0
                [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],  # 10
                [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],  # 20
                [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],  # 30
                [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],  # 40
                [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],  # 50
                [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],  # 60
                [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],  # 70
                [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],  # 80
                [1, 1, 1, 0, 1, 1, 0, 1, 1, 0],  # 90
            ],
            5,
        ),
    ]

    for grid, output in data:
        for func in funcs:
            assert func(grid) == output
