"""
Given an integer array nums where every element appears three times except
for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only
constant extra space.

Constraints:
    1 <= nums.length <= 3 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
    Each element in nums appears exactly three times except for one element
    which appears once.
"""

# Sofrido entender a solução genérica utilizando manipulação de bits. Há uma
# explicação bem completa nas soluções apresentadas pela comunidade:
#    https://leetcode.com/problems/single-number-ii/solutions/43295/detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers/

# Para o problema apresentado, a intuição pode ser simplificada um bocado

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return -1


def test_solution():
    """test"""

    funcs = [
        Solution().singleNumber,
    ]

    # fmt: off
    data = [
        ([2, 2, 3, 2], 3),
        ([0, 1, 0, 1, 0, 1, 99], 99),
    ]
    # fmt: on
    for nums, expected in data:
        for func in funcs:
            assert func(nums) == expected
