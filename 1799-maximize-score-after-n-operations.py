"""
You are given nums, an array of positive integers of size 2 * n. You must
perform n operations on this array.

In the ith operation (1-indexed), you will:

    Choose two elements, x and y.

    Receive a score of i * gcd(x, y).

    Remove x and y from nums.

Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.

Constraints:
    1 <= n <= 7
    nums.length == 2 * n
    1 <= nums[i] <= 10^6
"""

# Backtrack com memoization - para indexar cada situação (números utilizados),
# devemos utilizar um mapa de bits

from typing import List
import math

class Solution:

    def maxScore_backtrack(self, nums: List[int]) -> int:
        n = len(nums)
        num_states = 1 << n
        memo = [0] * num_states

        
        def backtrack(state, pairs_picked):
            if pairs_picked ==  n // 2:
                return 0

            if memo[state]:
                return memo[state]
            
            for i in range(n - 1):
                if state & 1 << i:
                    continue
                for j in range(i + 1, n):
                    if state & 1 << j:
                        continue
                    current = (pairs_picked + 1) * math.gcd(nums[i], nums[j])
                    next = backtrack(state | 1 << i | 1 << j, pairs_picked + 1)
                    memo[state] = max(memo[state], current + next)
            
            return memo[state]
        
        return backtrack(0, 0)


# Programação dinâmica com uma única dimensão - números utilizados, c
# onsolidados em um map de bits.

# Percorremos exaustivamente todoas as possibilidade começando a partir do
# último par até o primeiro. Cada conjuto de números utilizados será
# representada pelo mapa de bits e a melhor combinação destes números
# armazenada em um vetor indexado pelo mapa. O mapa de bits, portanto,
# corresponderá aos números já utilizados e o valor indexado pelo mapa
# corresponderá ao melhor valor possível a partir dos números disponíveis.
# Logo, o valor armazenado na posição (2 ** n) - 1, todos os bits setados,
# indicando não haver mais números disponíveis, será 0. Consequentemente o
# resultado desejado será armazenda na posição 0.

# Para calcularmos um valor associado a um estado, representado pelo mapa de
# bits, temos que analisar todos os pares possíveis de números disponíveis,
# calcular o valor dos pares, somá-lo à situação onde estes números não estão
# mais disponíveis (calculado previamente) e armazenar a melhor combinação.

    def maxScore_dp(self, nums: List[int]) -> int:
        n = len(nums)
        num_states = 1 << n
        final_state = num_states - 1
        dp = [0] * num_states
        dp[final_state] = 0

        def count_bits(map):
            count = 0
            while map:
                map &= map -1
                count += 1
            return count
        

        for state in range(final_state - 1, -1, -1):
            nums_picked = count_bits(state)
            if nums_picked % 2:
                continue
            
            for i in range(0, n-1):
                if state & 1 << i:
                    continue
                for j in range(i + 1, n):
                    if state & 1 << j:
                        continue
                    current = (nums_picked // 2 + 1) * math.gcd(nums[i], nums[j])
                    next = dp[state | 1 << i | 1 << j]
                    dp[state] = max(dp[state], current + next)
        
        return dp[0]

def test_solution():
    """test"""

    funcs = [
        Solution().maxScore_backtrack,
        Solution().maxScore_dp,
    ]

    data = [
        ([1, 2], 1),
        ([3, 4, 6, 8], 11),
        ([1, 2, 3, 4, 5, 6], 14),
    ]

    for nums, expected in data:
        for func in funcs:
            assert func(nums) == expected
