"""
You are given an encoded string s. To decode the string to a tape, the
encoded string is read one character at a time and the following steps are
taken:

    If the character read is a letter, that letter is written onto the tape.

    If the character read is a digit d, the entire current tape is repeatedly
    written d - 1 more times in total.

Given an integer k, return the kth letter (1-indexed) in the decoded string.

Constraints:
    2 <= s.length <= 100
    s consists of lowercase English letters and digits 2 through 9.
    s starts with a letter.
    1 <= k <= 10^9
    It is guaranteed that k is less than or equal to the length of the decoded 
    string.
    The decoded string is guaranteed to have less than 263 letters.
"""


class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        """
        Primeiro nós calculamos a string codificada até o ponto suficiente para
        obtermos a k-ésima letra. Deste processo obteremos o comprimento da string
        codificada, mesmo que parcial, e a posição final na string original que
        gerou a string codificada.

        Em seguida percorremos a string original ao contrário a partir da posição
        final encontrada na etapa anterior. Se o caracter em questão for um número,
        dividimos o comprimento da string codificada, também obtido na etapa
        anterior, pelo número. Como só calculamos a string codificada até o ponto
        estritamente necessário para obter a k-ésima letra, ao reduzirmos o
        comprimento da string estaremos "descartando" a letra desejada. No entanto,
        como o número na string original apenas replica a string construída até
        então, a matriz da letra descartada permanecerá na string codificada, cujo
        comprimento foi reduzido. A sua nova posição será o módulo de k pelo novo
        comprimento. Este procedimento será repetido toda vez que encontrarmos um
        número na string original.

        Caso encontremos uma letra, devemos decidir se ela ocupa a k-ésima posição,
        ajustada pela incidência de números em posições anteriores na string
        original, caso tenha ocorrido. Para tanto basta verificar se o módulo de k
        elo comprimento da string é igual a zero. Não podemos simplesmente comparar
        o comprimento da string com k, pois o ajuste do k na etapa anterior foi
        feito por meio do módulo com o comprimento da string. Portanto, se k for
        igual ao comprimento o seu módulo entre os dois será 0 e não o comprimento.
        Caso não seja, o comprimento da string será decrescido de 1.
        """

        return ""


def test_solution():
    """test"""

    funcs = [
        Solution().decodeAtIndex,
    ]

    # fmt: off
    data = [
        ['leet2code3', 10, 'o'],
        ['ha22', 5, 'h'],
        ['a2345678999999999999999', 1, 'a'],
        ['a2b3c4d5e6f7g8h9', 9, 'b'],
    ]
    # fmt: on

    for s, k, expected in data:
        for func in funcs:
            assert func(s, k) == expected


if __name__ == "__main__":
    pass
