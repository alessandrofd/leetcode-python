"""
The variance of a string is defined as the largest difference between
the number of occurrences of any 2 characters present in the string. Note
the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return
the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.

Constraints:
    1 <= s.length <= 10^4
    s consists of lowercase English letters.
"""

# O algoritmo de Kadane resolve o problema da máxima soma de um subarray.

# Considerando cada dupla de letras e atribuindo a elas os valores +1 e -1,
# podemos utilizaro o algoritmo de Kadane para resolver o problema.

# Temos que ter dois cuidados. Primeiro, não podemos contabilizar uma diferença
# entre ocorrência das letras sem que ambas estejam presentes. Segundo, não
# podemos zerar os contadores simplesmente quando a diferença entre
# as ocorrências for negativa. Em decorrência da necessidade da presença das
# duas letras, só podemos zerá-los quando ainda restar uma letra de valor
# negativa a ser processada.


from collections import defaultdict, Counter
from itertools import permutations


class Solution:
    def largestVariance(self, string: str) -> int:
        return 0

    # Podemos otimizar a solução filtrando apenas as ocorrências das letras da dupla
    # que estamos analizando.

    def largestVariance_filtered(self, string: str) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().largestVariance,
        Solution().largestVariance_filtered,
    ]

    # fmt: off
    data = [
        ('aababbb', 3),
        ('abcde', 0),
        ('abbaaabzaabaaaaaaaaaaaaa', 18),
    ]
    # fmt: on
    for string, expected in data:
        for func in funcs:
            assert func(string) == expected
