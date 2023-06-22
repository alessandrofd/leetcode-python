"""
You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:
    Choose an integer i such that 1 <= i < n and nums[i] > 0.
    Decrease nums[i] by 1.
    Increase nums[i - 1] by 1.

Return the minimum possible value of the maximum integer of nums after
performing any number of operations.

Constraints:
    n == nums.length
    2 <= n <= 10^5
    0 <= nums[i] <= 10^9
"""

# A ideia é uniformizar ao máximo os valores do vetor, logo o melor resultado
# possível é a média dos valores no vetor. Os valores são transferidos da
# esquerda para a direita. O ponto central para a resolução da questão é
# identificar os limites da transferência de valores.
#
# Se analisarmos o problema da direita para a esquerda, o objetivo torna-se
# transferir o maior valor possível para o lado esquerdo do vetor sem aumentar
# o seu valor médio. No entanto, caso a célula tenha um valor menor que a média,
# não haverá transferência e há a possibilidade do valor médio aumentar. Logo,
# a cada iteração é necessário calcular o valor possível de ser transferido e
# o valor médio da parcela do vetor ainda a ser processada e verificar se
# o mesmo não aumentou.
#
# Se processarmos o vetor da esquerda para direita e, a cada iteração,
# calcularmos o valor médio das células, processadas, simplificamos o problema
# dos limites de transferência descritos acima. Isto porque o que estabelece
# o limite para transferência são valores intermediários que, mesmo com
# os valores transferidos da direita para esquerda, não atingem o valor médio
# do vetor e, portanto, não conseguem transferir valores para o lado esquerdo
# sem aumentar a média. Nestes casos, o valor médio do lado esquerdo do vetor
# não será influenciado pelos valores do lado direito. A princípio,
# poderíamos parar o processamento assim que identificássemos o primeiro destes
# casos. No entanto, conseguimos indentificá-los apenas quando processamos o
# vetor de trás para a frente, logo, para identificar o primeiro, somos
# obrigados a processar todo o vetor. No entanto, se considerarmos por default
# que cada célula é um limite a transferência de valores para a esquerda e
# calcularmos o valor médio do vetor a medida que o percorremos da esquerda
# para a direita, ao término, o maior desses valores médios será a resposta
# esperada.
#
# Ambas abordagems tem complexidade O(n), no entanto, o processamento da
# esquerda para a direita é muito mais simples.

from math import ceil
from itertools import accumulate


class Solution:
    def minimizeArrayValue_loop(self, nums):
        prefix_sum = 0
        max_val = 0
        for i, num in enumerate(nums, 1):
            prefix_sum += num
            max_val = max(max_val, ceil(prefix_sum / i))

        return max_val

    def minimizeArrayValue_accumulate(self, nums):
        return max(ceil(acc / i) for i, acc in enumerate(accumulate(nums), 1))


def test_solution():
    """test"""

    funcs = [
        Solution().minimizeArrayValue_loop,
        Solution().minimizeArrayValue_accumulate,
    ]

    data = [
        ([3, 7, 1, 6], 5),
        ([10, 1], 10),
    ]

    for nums, output in data:
        for func in funcs:
            assert func(nums) == output
