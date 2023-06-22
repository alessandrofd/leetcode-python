"""
We can scramble a string s to get a string t using the following algorithm:

    If the length of the string is 1, stop.

    If the length of the string is > 1, do the following:

        Split the string into two non-empty substrings at a random index,
        i.e., if the string is s, divide it to x and y where s = x + y.

        Randomly decide to swap the two substrings or to keep them in the same
        order. i.e., after this step, s may become s = x + y or s = y + x.

        Apply step 1 recursively on each of the two substrings x and y.

Given two strings s1 and s2 of the same length, return true if s2 is
a scrambled string of s1, otherwise, return false.

Constraints:
    s1.length == s2.length
    1 <= s1.length <= 30
    s1 and s2 consist of lowercase English letters.
"""

# O resultado final é avaliarmos se a string s1 pode ser embaralhada segundo
# as regras postas pelo problema até tornar-se a string s2. Ao adotarmos
# a programação dinâmica como estratégia de resolução, temos que construir
# a solução do caso base, strings com um único caracter, até o objetivo final,
# as strings completas. A cada passo consideraremos como objeto de avaliação
# strings de comprimento crescente até chegarmos às strings originais.
#
# Portanto, na primeira iteração aplicaremos a regra de embaralhamento para
# um único caracter, ou seja, se as strings são idênticas. No entanto,
# as strings originais podem ter um comprimento maior do que um, logo teremos
# n possibilidade de strings unitárias, onde n é o comprimento das strings
# originais, extraídas de s1 e n de s2. Como os embaralhamentos subsequentes
# envolverão a troca de posições e de antemão não conhecemos quantas e quais
# trocas ocorrerão, teremos que verificar todas as combinações de strings
# possíveis. Logo, a viabilidade do embaralhamento nesta e nas subsequentes
# iterações será avaliada em três dimensões, o comprimento das strings e
# as strings propriamente ditas, descritas pelo índice de seu início nas
# strings originais e próprio comprimento.
#
# A cada iteração o tamanho das strings avaliadas será ampliado o que
# restringirá os valores possíveis de seus índices já que os limites das
# strings originais devem ser respeitados. Logo, os indíces variarão
# de 0 a n - length, onde length é o comprimento das strings na presente
# iteração. E a cada combinação de comprimento e índices, as várias
# possibilidades de fatiamento e troca de posições são avaliadas de forma a
# concluirmos se um string pode dar origem à outra.
#
# O fatiamento das strings dá origem a um novo par de strings menores que,
# devido à ordem em que a análise foi feita - da string unitária à string
# completa -, já foram avaliadas se são pares viáveis ou não. Logo, a cada
# iteração, a não ser a primeira em que os caracters são comparados
# diretamente, há uma avaliação centrada não no conteúdo das strings, mas no
# posicionamento de suas fatias, decorrente da inversão ou não das posições.
#
#    sendo:
#    n = comprimento das strings originais
#    length = comprimento das strings antes do fatiamento
#    i = índice de início da string antes de ser embaralhada
#    j = indíce de início da substring embaralhada
#    slice = comprimento da string da esquerda resultado do fatiamento, logo
#    string da direita terá comprimento igual a length - slice
#
#    dp[length][i][j] |= dp[slice][i][j] && dp[length-slice][i+slice][j+slice]
#    dp[length][i][j] |= dp[slice][i][j+length-slice] && dp[length-slice][i+slice][j]
#
# dp[length][i][j] indicará se há ao menos uma maneira de se embaralhar
# a substring s1[i:i+length] para que se torne a substring s2[j:j+length].
# O que não quer dizer necessariamente que este embaralhamento leve ao resultado
# final - s1[0:n] tornar-se s2[0:n], mas enquanto houver alternativas viáveis
# odemos continuar expandindo o tamanho das substrings analisadas aproximando
# ength de n e restringindo o espaço dos índices i e j até lhes restarem apenas 0.
#
# O caso base, em que não há fatiamento e tampouco inversão de posições, impede
# que incluamos essas variáveis na dimensões do dp. Logo, temos que consolidar
# todas as estratégias de embaralhamentos nas três dimensões restantes:
# comprimento e as duas string avaliadas.


class Solution:
    """Solution class"""

    def isScramble_dp(self, s1, s2):
        """Dynamic Programming"""

        n = len(s1)  # n = comprimento das strings originais
        dp = [[[False for j in range(n)] for i in range(n)] for l in range(n + 1)]

        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]

        for l in range(2, n + 1):  # l = comprimento das strings avaliadas
            for i in range(n - l + 1):  # i = início da string a ser embaralhada
                for j in range(n - l + 1):  # j = início da string embaralhada
                    for k in range(1, l):  # k = comprimento da fatia à esquerda
                        dp_left = dp[k][i]
                        dp_right = dp[l - k][i + k]
                        dp[l][i][j] |= dp_left[j] and dp_right[j + k]
                        dp[l][i][j] |= dp_left[j + l - k] and dp_right[j]

        return dp[n][0][0]

    # Outra alternativa é aplicar uma recursão top-down como se fosse um DFS.
    #  Neste caso partimos da string original e aplicamos a ela todas as
    # possibilidade de fatiamento - fatias de comprimento de 1 a n-1 (n sendo
    # o comprimento da string). Para cada uma destas fatias devem ser analisados
    # os cenários com e sem troca de posições. E em cada cenário teremos que
    # avaliar a viabilidade de dois conjuntos de string, a fatia da esqueda e a
    # da diretia. Logo, um fatiamento dará origem a 4 chamadas recursivas.

    memo = {}

    def isScramble_dfs(self, s1, s2):
        """DFS"""

        n = len(s1)
        if len(s2) != n:
            return False
        if s1 == s2:
            return True
        if n == 1:
            return False

        key = s1 + "#" + s2
        if key in self.memo:
            return self.memo[key]

        for i in range(1, n):  # i = comprimento da fatia à esquerda
            without_swap = self.isScramble_dfs(s1[:i], s2[:i]) and self.isScramble_dfs(
                s1[i:], s2[i:]
            )
            if without_swap:
                self.memo[key] = True
                return True

            with_swap = self.isScramble_dfs(
                s1[:i], s2[n - i :]
            ) and self.isScramble_dfs(s1[i:], s2[: n - i])
            if with_swap:
                self.memo[key] = True
                return True

        self.memo[key] = False
        return False


def test_solution():
    """test"""

    funcs = [Solution().isScramble_dp, Solution().isScramble_dfs]

    data = [
        ("great", "rgeat", True),
        ("abcde", "caebd", False),
        ("a", "a", True),
        ("abcdefghijklmnopq", "efghijklmnopqcadb", False),
    ]

    for s1, s2, output in data:
        for func in funcs:
            assert func(s1, s2) == output
