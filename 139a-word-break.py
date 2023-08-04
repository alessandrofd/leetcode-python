"""
Given a string s and a dictionary of strings wordDict, return true if s can
be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.

Constraints:
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        """
        Approach 4: Using Dynamic Programming

        A programação dinâmica é construída tendo como parâmentro o comprimento das
        substrings que atendem os requisitos do problema. A partir da substring de
        comprimento 0 - que, por definição, atende ao enunciado do problema,
        percorremos todo o comprimento da string. A cada passo verificamos se há
        alguma combinação de substrings anteriores que podem ser compostas a partir
        das palavras do dicionário e substrings que correspondam a alguma palavra do
        dicionário. Caso estas condições sejam atendidas, consideramos que a
        substring de comprimento que estamos analisando atende ao enunciado do
        problemas e esta se torna candidata a compor nova substring válida nas
        próximas iterações. Ao fim nos interessa saber se a string de comprimento
        igual à string original, ou seja, a própria string original é válida, pois
        pode ser formada por substrings menores consideradas válidas em iterações
        anteriores e alguma palavra no dicionário.

        Dimensão: comprimento da string,
        Caso base: dp[0] = true
        Transição: para 1 <= i <= n e 0 <= j < i , dp[i] |= dp[j] && s[j:i] in map
        Solução: dp[n]
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        words_set = set(words)

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words_set:
                    dp[i] = True
                    break
        return dp[n]


def test_solution():
    """test"""

    funcs = [
        Solution().wordBreak,
    ]

    # fmt: off
    data = [
        ('leetcode', ['leet', 'code'], True),
        ('applepenapple', ['apple', 'pen'], True),
        ('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'], False),
    ]
    # fmt: on
    for s, word, expected in data:
        for func in funcs:
            assert func(s, word) == expected


if __name__ == "__main__":
    pass
