"""
Given an array arr of positive integers sorted in a strictly increasing
order, and an integer k.
Return the kth positive integer that is missing from this array.
Constraints:
    1 <= arr.length <= 1000
    1 <= arr[i] <= 1000
    1 <= k <= 1000
    arr[i] < arr[j] for 1 <= i < j <= arr.length
"""

from typing import List


class Solution:
    """Solution class"""

    def findKthPositive_brute(  # pylint: disable=invalid-name
        self, arr: List[int], k: int
    ) -> int:
        """Brute force"""

        # À medida que vamos analisando as diversas situações: k antes do vetor e
        # k no vetor, o valor de k vai sendo atualizado. Até que no final, k depois
        # do vetor, basta retornar o valor do último elemento acrescido do saldo
        # de k

        n = len(arr)

        if k <= arr[0] - 1:
            return k

        k -= arr[0] - 1

        for i in range(n - 1):
            missing = arr[i + 1] - arr[i] - 1
            if missing >= k:
                return arr[i] + k
            k -= missing

        return arr[-1] + k

    def findKthPositive_binSearch(  # pylint: disable=invalid-name
        self, arr: List[int], k: int
    ) -> int:
        """Binary Search"""

        # A quantidade de elementos não presentes antes de um elemento na
        # posição i é igual a arr[i] - (i + 1)

        lo = 0
        hi = len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] - (mid + 1) < k:
                lo = mid + 1
            else:
                hi = mid - 1

        # Ao término do laço lo = hi + 1 e o elemento que estamos procurando
        # estará entre arr[hi] e arr[lo]
        # O valor a ser retornado será igual a:
        #     arr[hi] + (k - (arr[hi] - (hi + 1))) =>
        #     arr[hi] + k - arr[hi] + hi + 1 =>
        #     (hi + 1) + k =>
        #     lo + k
        return lo + k


funcs = [Solution().findKthPositive_brute, Solution().findKthPositive_binSearch]

data = [
    ([2, 3, 4, 7, 11], 5, 9),
    ([1, 2, 3, 4], 2, 6),
    ([5, 6, 7], 3, 3),
    ([1, 10, 21, 22, 25], 12, 14),
    ([2], 1, 1),
]

for arg_arr, arg_k, output in data:
    print(f"arr = {arg_arr}, k = {arg_k}\nOutput = {output}")
    for func in funcs:
        print(f"{func.__name__} = {func(arg_arr, arg_k)}")
