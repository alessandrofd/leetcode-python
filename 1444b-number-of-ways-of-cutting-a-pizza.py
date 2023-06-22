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
