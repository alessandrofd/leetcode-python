"""
Given the integers zero, one, low, and high, we can construct a string by
starting with an empty string, and then at each step perform either of
the following:

    Append the character '0' zero times.

    Append the character '1' one times.

This can be performed any number of times.

A good string is a string constructed by the above process having a length
between low and high (inclusive).

Return the number of different good strings that can be constructed
satisfying these properties. Since the answer can be large, return it
odulo 10^9 + 7.

Constraints:
    1 <= low <= high <= 10^5
    1 <= zero, one <= low
"""


# Programação dinâmica com uma única dimensão: a quantidade de caracteres na
# string final. limitado a high (inclusive)
# Caso base: dp[0] = 0, dp[one] += 1, dp[zero] += 1
# Transição: dp[i] += (dp[i-one] se i >= one == 0) + (dp[i-zero] se i >=  zero)
# Resultado final: sum(dp[low:high])

# Podemos ajustar a condição inicial para dp[0] = 1, neste caso quando
# i >= zero ou one o valor inicial será recuperado de dp[0] e não de dp[zero] e
# dp[one], respectivamente.

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        return 0

def test_solution():
    """test"""

    funcs = [
        Solution().countGoodStrings,
    ]

    data = [
        (3, 3, 1, 1, 8),
        (2, 3, 1, 2, 5),
    ]

    for low, high, zero, one, expected in data:
        for func in funcs:
            assert func(low, high, zero, one) == expected
