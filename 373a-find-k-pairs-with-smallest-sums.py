"""
You are given two integer arrays nums1 and nums2 sorted in ascending order
and an integer k.

Define a pair (u, v) which consists of one element from the first array and
one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Constraints:
    1 <= nums1.length, nums2.length <= 10^5
    -10^9 <= nums1[i], nums2[i] <= 10^9
    nums1 and nums2 both are sorted in ascending order.
    1 <= k <= 10^4
"""


# Utiliza uma fila de prioridade max e inclui nela todas as possibilidade de
# combinação ou seja k^2 elementos. A fila é sempre mantida com um comprimento
# máximo de k

### Solução intermediária


# Utiliza uma fila de prioridades min. Seleciona-se o primeiro elemento da fila,
# caracterizado pelos índices de cada um dos vetores nums1 e nums1, e insere
# a tupla na resposta. Avança os índices um de cada vez e enfileira
# a combinação caso já não tenha sido. Essas operação são repetidas k vezes ou
# até que a fila se esvazie.

# Estourou a pilha de memória no JS

### Solução intermediária

# Otimização da solução anterior

# Considerando os índices i e j recém selecionados como parte da solução,
# ou seja nums1[i] + nums2[j] é o menor valor dentre as combinações disponíveis.
# Só faz sentido consdiderarmos a combinação (i+1, j) se j for igual a zero,
# pois qualquer outro valor de j resultará em uma combinação de valor maior que
# nums1[i+1] + nums2[0] e, portanto, só deve ser levada em consideração após
# i+1, 0). No entanto, entre (i, 0) e (i+1, 0), temos que considerar todas
# as combinações de (i,j) onde j > 0 que produzam valores menores que (i+1, 0).

# Existe uma dificuldade natural na compreensão desta solução pois procuramos
# resultados menores (nums1[i] + nums2[j]) à medida que os índices aumentam.

from typing import List
from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        n1 = len(nums1)
        n2 = len(nums2)

        heap = [(nums1[0] + nums2[0], 0, 0)]
        result = []
        while len(result) < k and len(heap) > 0:
            _, idx1, idx2 = heappop(heap)
            result.append([nums1[idx1], nums2[idx2]])

            if idx1 + 1 < n1 and idx2 == 0:
                heappush(heap, (nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2))

            if idx2 + 1 < n2:
                heappush(heap, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))

        return result


def test_solution():
    """test"""

    funcs = [
        Solution().kSmallestPairs,
    ]

    # fmt: off
    data = [
        ([1, 7, 11], [2, 4, 6], 3, [[1,2],[1,4],[1,6]]),
        ([1, 1, 2], [1, 2, 3], 2, [[1,1],[1,1]]),
        ([1, 2], [3], 3, [[1,3],[2,3]]),
        ([1, 1, 2], [1, 2, 3], 10, [[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]),
    ]
    # fmt: on
    for nums1, nums2, k, expected in data:
        for func in funcs:
            assert sorted(func(nums1, nums2, k)) == sorted(expected)
