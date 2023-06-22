"""
You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of
the minimum and maximum element on it is less or equal to target. Since
the answer may be too large, return it modulo 10^9 + 7.

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^6
    1 <= target <= 10^6
"""

# A quantidade de subsequences de um array de comprimento n é 2^n.
# Inicialmente ordenamos o array. Utilizaremos dois ponteiros que percorrerão o
# array ordenado em direções opostas. Caso a soma dos valores apontados pelos
# ponteiros, que, graças ao ordenamento, corresponderão aos valores mínimo e
# máximo do subarray delimitado pelos ponteiros, for menor ou igual ao alvo,
# acresentaremos ao resultado a quantidade de subsequences do subarray, cujo
# comprimento será a diferencça entre os ponteiros. Em seguida avançaremos
# o ponteiro da esquerda. No entanto, se a soma for superior ao alvo, apenas
# recuaremos o ponteiro da direita.
#
# Dado o valor exponencial do resultados, cuidado adicional deve ser tomado na
# construção do resultado. Notamos que dadas as dimensões do problema,
# inclusive as funções matemáticas do Javascript apresentaram resultados
# espúrios. Logo, foi necessário construir um vetor com as potências de 2 até o
# comprimento do vetor com os valores já modularizados.

from typing import List


class Solution:
    """solution class"""

    def numSubseq(self, nums: List[int], target: int) -> int:
        """solution method"""
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().numSubseq,
    ]

    data = [
        ([3, 5, 6, 7], 9, 4),
        ([3, 3, 6, 8], 10, 6),
        ([2, 3, 3, 4, 6, 7], 12, 61),
    ]

    for nums, target, expected in data:
        for func in funcs:
            assert func(nums, target) == expected
