"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining
elements.

Constraints:
    1 <= s.length <= 1000
    s consists only of lowercase English letters.
"""

# A ideia central é que se analisarmos string de fora para dentro, primeiro e
# último caracteres para começar, e se os caracteres analisados forem iguais,
# eles comporão o palíndromo mais comprido, independente do restante da string.
# Logo, podemos analisar recursivamente a string com o apoio de dois ponteiros,
# incializados para apontarem para o início e final da string. Caso
# os caracteres apontados pelos ponteiros forem iguais, retornaremos 2
# (correspondente aos caracteres iguais) mais o resultado do processamento
# recursivo da string, avançando o ponteiro da esquerda em uma posição e
# recuando o da direita. Caso os caracteres não sejam iguais, teremos que
# explorar dois cenários distintos e selecionar aquele que produzir
# o palíndromo mais comprido. Os cenários são obtidos avançando o ponteiro
# da esquerda e mantendo o da direita parado e vice-versa. Este processo é
# repetido até que atinjamos a condição de saída da recursão, a saber,
# o ponteiro da esquerda se igualar ou ultrapassar o ponteiro da direita.
# Para otimizar o algoritmo, aplicamos memoization.


class Solution:
    def longestPalindromeSubseq_recursion(self, s):
        pass

    # Podemos aplicar programação dinâmica considerando duas dimensões distintas,
    # os índices de início e fim relativos que definem uma subsequência em relação
    # à string original. São dois os casos base: subsequências unitárias contribuem
    # com um único caracter ao palíndromo final, logo dp[i][i] == 1.
    # E subsequências em que o término seja menor que o início são inválidas e,
    # portanto, não contribuem ao palíndromo, logo dp[i][j] == 0 quando j < i.

    # As transições são funções dos valores dos caracteres nas extremidades
    # da subsequência. Caso sejam iguais, o valor da iteração será igual a 2 mais
    # o valor da subsequência interna às extremidades, ou seja,
    # dp[i][j] = 2 + dp[i+1][j-1]. Caso sejam distintos, o valor da iteração será
    # o maior valor produzido pela subsequência obtida após o descarte do caracter
    # no início, dp[i+1][j], e por aquela obtida com o descarte do caracter
    # no final, dp[i][j-1]

    # Partimos da menor subsequência possível, o último caracter da string,
    # e expandimos a seleção até considerarmos toda a string. A cada iteração
    # do ponteiro do início da subsequênia, o ponteiro do final percorrerá todas
    # s posição, desde a posição seguinte ao início da subsequência. até o término
    # da string. Sequindo esta sequência, além de contemplar todas as possibilidades
    # de subsequências, garantimos que, a cada passo da programação dinâmica,
    # eremos os elementos necessários para o cálculo do seu valor.

    # O resultado será representado na posição 0, n-1, onde n representa
    # o comprimento da string.

    def longestPalindromeSubseq_DP(self, s):
        pass


def test_solution():
    """test"""

    funcs = [
        Solution().longestPalindromeSubseq_recursion,
        Solution().longestPalindromeSubseq_DP,
    ]

    data = [
        ("bbbab", 4),
        ("cbbd", 2),
    ]

    for s, output in data:
        for func in funcs:
            assert func(s) == output
