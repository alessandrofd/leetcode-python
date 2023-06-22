"""
You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

    target should be formed from left to right.

    To form the ith character (0-indexed) of target, you can choose
    the kth character of the jth string in words if target[i] = words[j][k].

    Once you use the kth character of the jth string of words, you can no
    longer use the xth character of any string in words where x <= k. In other
    words, all characters to the left of or at index k become unusuable for
    every string.

    Repeat the process until you form the string target.

Notice that you can use multiple characters from the same string in words
provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be
too large, return it modulo 10^9 + 7.

Constraints:
    1 <= words.length <= 1000
    1 <= words[i].length <= 1000
    All strings in words have the same length.
    1 <= target.length <= 1000
    words[i] and target contain only lowercase English letters.
"""

# Programação dinâmica
# Podemos considerar as palavras como uma matriz

# Duas dimensões: posição da letra de alvo e a quantidade de colunas da matriz
# de palavras das quais selecionamos letras para formar o alvo

# Caso base: Se não utilizarmos nenhuma coluna a quantidade de alternativas
# será 0 => dp[0] = [0] * quantidade de letras em target

# Transição: dp[coluna][letra] = dp[coluna-1][letra] + (dp[coluna-1][letra-1] * somatório de palavras[*][coluna] == alvo[letra])

# Resultado final: somatário de dp[quantidade de colunas][comprimento de target]

# Otimizar a contagem do somatário de alternativas em cada coluna por meio de
# uma tabela de frequências se letras em cada coluna. Limitar o laço de colunas
# ao valor mínimo entre a coluna analisada e a quantidade de letras

from collections import Counter


class Solution:
    def numWays_dp(self, words, target):
        MOD = 1e9 + 7

        n = len(target)
        rows = len(words)
        cols = len(words[0])

        dp = [[0 for _ in range(n)] for _ in range(cols + 1)]

        freqs = [Counter(letters) for letters in zip(*words)]

        for col in range(1, cols + 1):
            for letter in range(min(n, col)):
                freq = freqs[col - 1][target[letter]]
                product = freq if letter == 0 else dp[col - 1][letter - 1] * freq
                dp[col][letter] = int((dp[col - 1][letter] + product) % MOD)

        return dp[cols][n - 1]

    # Otimizar a programação dinâmica ao utilizar um vetor para armazenar valores
    # intermediários.
    #
    # Podemos perceber que a solução baseada em programação dinâmica, a cada iteração das colunas, utiliza apenas as informações da coluna anterior. Logo, não há a necessidade de armazernarmos todas a matriz. Uma das alternativas é utilizar dois vetores, um contendo os dados da coluna anterior e outro da coluna sob processamento. No entanto, se invertermos a ordem de processamento das letras do alvo, talvez seja possível trabalhar com um único vetor.

    def numWays_dp_optimized(self, words, target):
        MOD = 1e9 + 7

        n = len(target)
        cols = len(words[0])

        freqs = [Counter(letters) for letters in zip(*words)]

        row = [0] * n
        for col in range(1, cols + 1):
            for letter in range(min(n, col) - 1, -1, -1):
                freq = freqs[col - 1][target[letter]]
                product = freq if letter == 0 else row[letter - 1] * freq
                row[letter] = int((row[letter] + product) % MOD)

        return row[n - 1]

    # DFS utilizando os casos base da DP como condições de saída da recursão e
    # as transições como retorno da função recursiva

    def numWays_dfs(self, words, target):
        MOD = 1e9 + 7

        n = len(target)
        cols = len(words[0])

        memo = [[None for _ in range(n)] for _ in range(cols)]
        freqs = [Counter(letters) for letters in zip(*words)]

        def dfs(col, letter):
            if col < 0 or letter > col:
                return 0
            if memo[col][letter]:
                return memo[col][letter]

            freq = freqs[col][target[letter]]
            product = freq if letter == 0 else dfs(col - 1, letter - 1) * freq
            memo[col][letter] = int((dfs(col - 1, letter) + product) % MOD)

            return memo[col][letter]

        return dfs(cols - 1, n - 1)


def test_solution():
    """test"""

    funcs = [
        # Solution().numWays_dp,
        # Solution().numWays_dp_optimized,
        Solution().numWays_dfs,
    ]

    data = [
        (["acca", "bbbb", "caca"], "aba", 6),
        (["abba", "baab"], "bab", 4),
    ]

    for words, target, output in data:
        for func in funcs:
            assert func(words, target) == output
