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
from collections import defaultdict


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
        n = ceil(ml / 25)

        dp = [{0: 0.5}]

        def solve(a, b):
            servings = [(4, 0), (3, 1), (2, 2), (1, 3)]
            result = 0
            for i, j in servings:
                result += dp[max(0, a - i)][max(0, b - j)]
            return result / 4

        for a in range(1, n + 1):
            dp[0][a] = 1
            dp.append({0: 0})

            for b in range(1, a + 1):
                dp[a][b] = solve(a, b)
                dp[b][a] = solve(b, a)

            if dp[a][a] > 1 - 1e-5:
                return 1.0

        return dp[n][n]

    def soupServings_top_down_large_numbers(self, ml: int) -> float:
        n = ceil(ml / 25)

        @cache
        def solve(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0

            servings = [(4, 0), (3, 1), (2, 2), (1, 3)]
            result = 0
            for i, j in servings:
                result += solve(a - i, b - j)
            return result / 4

        for i in range(1, n + 1):
            if solve(i, i) > 1 - 1e-5:
                return 1.0

        return solve(n, n)


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
