"""
You are given a 0-indexed integer array nums and an integer p. Find p pairs
of indices of nums such that the maximum difference amongst all the pairs is
minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this
pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the
maximum of an empty set to be zero.

Constraints
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
    0 <= p <= (nums.length)/2
"""

from typing import List
from bisect import bisect_left


class Solution:
    def minimizeMax(self, nums: List[int], num_pairs: int) -> int:
        """
        Greedy + busca binária

        Neste caso a busca binária não será por uma posição em um lista ordenada, mas
        pela própria resposta. Considerando uma lista ordenada de valores de
        comprimento n, as respostas válidas estarão entre 0 e abs(nums[n-1] - nums[0]).
        Devemos buscar entre estes valores o menor em que haja no mínimo o número de
        pares solicitados cuja diferença seja menor ou igual o valor buscado.

        Para determinarmos a quantidade de pares cuja diferença seja menor ou igual
        ao valor buscado, utilizamos uma abordagem greedy. Percorremos toda a lista
        ordenada e caso um par seja menor ou igual ao valor buscado, contabilizamos a
        sua ocorrência e pulamos 2 posições. Caso contrário, apenas pulamos uma
        posição. Assim que o número mínimo de pares é encontrado, retornamos
        verdadeiro. Caso percorramos toda a lista sem encontrar o número mínimo de
        pares, retornamos falso.
        """
        if num_pairs == 0:
            return 0

        n = len(nums)

        def enough_pairs(threshold):
            count_pairs = 0
            i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= threshold:
                    count_pairs += 1
                    i += 1
                    if count_pairs >= num_pairs:
                        return True
                i += 1
            return False

        nums.sort()
        sorted_unique_diffs = sorted({nums[i + 1] - nums[i] for i in range(n - 1)})
        lo = sorted_unique_diffs[0]
        hi = sorted_unique_diffs[-1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if not enough_pairs(mid):
                lo = mid + 1
            else:
                hi = mid

        return lo

    def minimizeMax_bisect(self, nums: List[int], num_pairs: int) -> int:
        """
        Mesma lógica da solução anterior, apenas utilizando bisect
        Para tanto a função que valida que haja o pares suficientes cuja
        diferença seja menor ou igual à solicitada tem que ser modificada. Na
        versão anterior a função apenas indica se há pares suficiente sem se
        importar com a quantidade propriamente dita - inclusive isto permite que
        otimizemos a função retornando assim que o número de pares solcitado
        seja atingido. Para utilizar o bisect, a função passará a retornar a
        quantidade de pares cuja a diferença seja menor ou igual à solicitada.
        Como consequência, toda a lista de números terá que ser percorrida.
        """
        if num_pairs == 0:
            return 0

        n = len(nums)

        def num_valid_pairs(threshold):
            count_pairs, i = 0, 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= threshold:
                    count_pairs += 1
                    i += 1
                i += 1
            return count_pairs

        nums.sort()
        sorted_unique_diffs = sorted({nums[i + 1] - nums[i] for i in range(n - 1)})
        i = bisect_left(sorted_unique_diffs, num_pairs, key=num_valid_pairs)
        return sorted_unique_diffs[i]


def test_solution():
    """test"""

    funcs = [
        Solution().minimizeMax,
        Solution().minimizeMax_bisect,
    ]

    # fmt: off
    data = [
        ([10, 1, 2, 7, 1, 3], 2, 1),
        ([4, 2, 1, 2], 1, 0),
        ([0, 5, 3, 4], 0, 0)
    ]
    # fmt: on
    for nums, num_pairs, expected in data:
        for func in funcs:
            assert func(nums, num_pairs) == expected


if __name__ == "__main__":
    Solution().minimizeMax_bisect([10, 1, 2, 7, 1, 3], 2)
