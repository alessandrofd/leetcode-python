"""
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""

# A intuição utilizada na solução é considerar cada valor do vetor não como
# o início de um subvetor, mas como o seu término. Desta forma, contamos
# a quantidade de subvetores dos quais a célula com valor zero é o término.
# Para tanto, temos que acumular a quantidade de subvetores à medida que
# encontramos zeros encadeados. Quando encontramos um zero pela primeira vez,
# ou que não tenha sido imediatamente antecedido por outro zero, ele será
# o término de um único subvetor composto apenas pela célula que estamos
# examinando. Assim, somomamo ao resultado final este único subvetor. Caso
# a próxima célula não seja um zero, temos que zerar a contagem de subarray.
# Caso contrário, esta nova célula será término do subvetor composto
# exclusivamente por ela e de todos os subvetores dos quais a célula anterior
# foi o término. Portanto, devemos atualizar a contagem de subvetores e somá-la
# o resultado final.

from typing import List


class Solution:
    """Solution class"""

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """Solution func"""


def test_solution():
    """test"""

    funcs = [Solution().zeroFilledSubarray]

    data = [
        ([1, 3, 0, 0, 2, 0, 0, 4], 6),
        ([0, 0, 0, 2, 0, 0], 9),
        ([2, 10, 2019], 0),
    ]

    for nums, output in data:
        for func in funcs:
            assert func(nums) == output
