"""
Given a rectangular pizza represented as a rows x cols matrix containing
the following characters: 'A' (an apple) and '.' (empty cell) and given
the integer k. You have to cut the pizza into k pieces using k-1 cuts.

For each cut you choose the direction: vertical or horizontal, then you
choose a cut position at the cell boundary and cut the pizza into two pieces.
If you cut the pizza vertically, give the left part of the pizza to a person.
If you cut the pizza horizontally, give the upper part of the pizza to
a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains
at least one apple. Since the answer can be a huge number, return this
modulo 10^9 + 7.

Constraints:
    1 <= rows, cols <= 50
    rows == pizza.length
    cols == pizza[i].length
    1 <= k <= 10
    pizza consists of characters 'A' and '.' only.
"""


# Programamção dinâmica com uma matrix tridimensional com as seguintes
# dimensões: cortes restantes e linha e coluna do pedaço restanted da pizza
# após os cortes.
#
# Caso base, após todos os cortes deve restar pelo menos uma maçã no pedaço
# final. Ou seja, dp[0][row][col] > 0
#
# Caso final dp[k-1][0][0], pizza inteira(row = 0 e col = 0) como todos os
# cortes ainda a serem feitos (remain = k -1 )
#
# Transiçao de k para k - 1, o pedaço resutante do corte será definido por nova
# linha ou coluna (newRow ou newCol), logo dp[k][row][col] será a somatória
# dos dp[k-1][newRow][col] e dp[k-1][row][newCol] (onde row < newRow < rows e
# col < newCol < cols), válidos, ou seja em que o pedaço cortado tenha ao menos
# uma maçã.


class Solution:
    """Solution class"""

    def ways(self, pizza, k):
        """Dynamic Programming"""

        MOD = 10**9 + 7
        rows = len(pizza)
        cols = len(pizza[0])

        apples = [[0 for col in range(cols + 1)] for row in range(rows + 1)]
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                apples[row][col] = (
                    (pizza[row][col] == "A")
                    + apples[row][col + 1]
                    + apples[row + 1][col]
                    - apples[row + 1][col + 1]
                )

        dp = [
            [[0 for col in range(cols)] for row in range(rows)] for remain in range(k)
        ]

        # Caso base - não tem transição, basta garantir que o pedaço de pizza,
        # [row][col] tenha ao menos uma maçã
        dp[0] = [
            [int(apples[row][col] > 0) for col in range(cols)] for row in range(rows)
        ]

        # Transições
        for remaining_cuts in range(1, k):
            for row in range(rows):
                for col in range(cols):
                    valid_cuts = 0
                    # corte horizontal
                    for new_row in range(row + 1, rows):
                        if apples[row][col] - apples[new_row][col] > 0:
                            valid_cuts += dp[remaining_cuts - 1][new_row][col]

                    # corte vertical
                    for new_col in range(col + 1, cols):
                        if apples[row][col] - apples[row][new_col] > 0:
                            valid_cuts += dp[remaining_cuts - 1][row][new_col]

                    dp[remaining_cuts][row][col] = valid_cuts % MOD

        return dp[k - 1][0][0]


def test_solution():
    """test"""

    funcs = [Solution().ways]

    data = [
        (["A..", "AAA", "..."], 3, 3),
        (["A..", "AA.", "..."], 3, 1),
        (["A..", "A..", "..."], 1, 1),
    ]

    for pizza, k, output in data:
        for func in funcs:
            assert func(pizza, k) == output


if __name__ == "__main__":
    Solution().ways(["A..", "AAA", "..."], 3)
