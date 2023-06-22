"""
Given a string s. In one step you can insert any character at any index of
the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters.
"""

# A chave para a resolução do problema é achar o comprimento da subsequência
# palindrômica mais longa da string original. Como o problema permite inserirmos
# qualquer caracter em qualquer posição da string, a resposta será a diferença
# entre comprimento da string e o comprimento da subsequência palindrômica.


class Solution:
    def minInsertions_recursion(self, normal_string):
        pass

    # Uma solução utilizando programação dinâmica pode aproveitar os elementos da
    # solução recursiva. O objetivo continua o mesmo, achar o comprimento da mais
    # longa subsequência palidrômica e retornar a diferença entre ela e o
    # comprimento da string original. A programação dinâmica requrerá duas
    # dimensãoes, os comprimentos das strings normais e invertidas, tal qual o
    # memoization da solução recursiva. O caso base corresponderá à condição de
    # saída da recursão, strings com comprimento 0 produzem subsequências também de
    # comprimento 0. Por fim, as transições da DP corresponderão ao processamento
    # feito a cada iteração recursiva:
    #    se string[i] === reverse[j] => dp[i][j] = dp[i-1][j-1]
    #    senão => dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    #    onde i e j são ponteiros para a string original e invertida,
    #    respectivamente, limitados ao comprimento total da string original
    #
    # O comprimento da mais comprida subsequência palindrômica será dado por
    # dp[n][n], onde n é o comprimento da string original

    def minInsertions_dp(self, normal_string):
        pass


def test_solution():
    """test"""

    funcs = [
        Solution().minInsertions_recursion,
        Solution().minInsertions_dp,
    ]

    data = [
        ("zzazz", 0),
        ("mbadm", 2),
        ("leetcode", 5),
    ]

    for normal_string, expected in data:
        for func in funcs:
            assert func(normal_string) == expected
