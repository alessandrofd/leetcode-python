"""
There are two types of soup: type A and type B. Initially, we have n ml of
each type of soup. There are four kinds of operations:

    1. Serve 100 ml of soup A and 0 ml of soup B,
    2. Serve 75 ml of soup A and 25 ml of soup B,
    3. Serve 50 ml of soup A and 50 ml of soup B, and
    4. Serve 25 ml of soup A and 75 ml of soup B.

When we serve some soup, we give it to someone, and we no longer have it.
Each turn, we will choose from the four operations with an equal probability
0.25. If the remaining volume of soup is not enough to complete the operation,
we will serve as much as possible. We stop once we no longer have some
quantity of both types of soup.

Note that we do not have an operation where all 100 ml's of soup B are used
first.

Return the probability that soup A will be empty first, plus half the
probability that A and B become empty at the same time. Answers within 10-5
f the actual answer will be accepted.

Constraints:
    0 <= n <= 10^9
"""

from math import ceil
from functools import cache


class Solution:
    def soupServings_bottom_up_large_numbers(self, ml: int) -> float:
        """
        Programação dinâmica
        Dimensões: Quantas porções de cada sopa ainda restam.
        Caso base: Sopa A zerada equivale a 100% e as duas sopas zerada equivale a 50%.
        Logo, o processo será invertido, calcularemos as probabilidades não ao servir
        a sopa mas ao retornar a sopa
        Transição: dp[sopaA][sopaB] += dp[sopaA - porcaoA][sopaB - porcaoB] / 4
        (há 4 combinações possível, por isso dividir a probabilidade por 4)
        Resultado final: dp[n][n]

        Como as alternativas de servir sopa não são simétricas, não há a
        possibilidade de servir 100ml da sopa B e nada da sopa A, a tedência, dadas
        iterações suficientes é que a sopa A termine antes da sopa B. Ou seja,
        considerando a lei dos grandes números a resposta será 1, desde que haja uma
        quantidade de iterações que nos leve suficientemente perto de 1. O próprio
        problema nos dá o fator de aproximação: 10:-5
        """
        return 0.0

    def soupServings_top_down_large_numbers(self, ml: int) -> float:
        return 0.0


def test_solution():
    """test"""

    funcs = [
        Solution().soupServings_bottom_up_large_numbers,
        Solution().soupServings_top_down_large_numbers,
    ]

    # fmt: off
    data = [
    (50, 0.62500),
    (100, 0.71875),
    ]
    # fmt: on
    for ml, expected in data:
        for func in funcs:
            assert func(ml) == expected
