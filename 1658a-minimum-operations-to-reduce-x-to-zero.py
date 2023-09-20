"""
You are given an integer array nums and an integer x. In one operation, you
can either remove the leftmost or the rightmost element from the array nums
and subtract its value from x. Note that this modifies the array for future
operations.

Return the minimum number of operations to reduce x to exactly 0 if it is
possible, otherwise, return -1.

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4
    1 <= x <= 10^9
"""


class Solution:
    def minOperations_dict(self, nums: list[int], x: int) -> int:
        """
        Ao invés de tentar as combinações no início e no final no array,
        nós tentamos descobrir qual o maior subarray cuja somatória de seus valores é
        a diferença entre o parâmetro x e a somatória de todos os elementos do vetor.
        Este será o nosso valor alvo.

        Percorremos o vetor totalizando os seus valores. Como o percorremos da
        esquerda para a direita, podemos considerar que cada iteração corresponde a
        uma supressão, cada vez menor, de elementos à direita. Utilizamos uma mapa
        para armazenar o índice das somas parciais do vetor. A cada passo testamos se
        já houve uma soma parcial anterior que quando subtraída da soma atual
        corresponde ao valor alvo. Caso o teste seja possitivo, o valor armazenado no
        mapa corresponderá aos elementos à esquerda a serem eliminados. Por outro
        lado, o próprio índice da iteração marca o limite do subarray, ou seja, os
        elementos à direita não devem ser considerados para que obtenhamos o valor
        desejado.

        Como é possível que haja mais de um subarray cuja soma de valores seja igual
        ao valor que procuramos, devemos percorrer todo vetor. Toda vez que acharmos
        um subarray válido, devemos testar se o seu comprimento é maior que os dos
        demais subarrays válidos. O seu comprimento será igual ao índice da iteração
        menos os elementos à esquerda a serem eliminado - valor armazenado no mapa.
        """
        n = len(nums)
        total = sum(nums)
        if total == x:
            return n

        target = total - x
        index_by_sum = {}
        index_by_sum[0] = -1

        prefix_sum = 0
        max_len = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum - target in index_by_sum:
                max_len = max(max_len, i - index_by_sum[prefix_sum - target])
            index_by_sum[prefix_sum] = i

        if max_len == 0:
            return -1
        return n - max_len

    def minOperations_pointers(self, nums: list[int], x: int) -> int:
        """
        Aqui usamos explicitamente dois ponteiros que indicarão os limites do
        subarray. Avançamos primeiramente o ponteiro da direita e assim que o
        somatório do subarray extrapolar o valor alvo, avançamos o ponteiro da
        esquerda.
        """
        n = len(nums)
        total = sum(nums)
        if total == x:
            return n

        target = total - x
        max_len = 0
        win_sum = 0
        left = 0
        for right in range(n):
            win_sum += nums[right]
            while left <= right and win_sum > target:
                win_sum -= nums[left]
                left += 1

            if win_sum == target:
                max_len = max(max_len, right - left + 1)

        if max_len == 0:
            return -1
        return n - max_len


def test_solution():
    """test"""

    funcs = [
        Solution().minOperations_dict,
        Solution().minOperations_pointers,
    ]

    # fmt: off
    data = [
        [[1, 1, 4, 2, 3], 5, 2],
        [[5, 6, 7, 8, 9], 4, -1],
        [[3, 2, 20, 1, 1, 3], 10, 5],
    ]
    # fmt: on

    for nums, x, expected in data:
        for func in funcs:
            assert func(nums, x) == expected


if __name__ == "__main__":
    pass
