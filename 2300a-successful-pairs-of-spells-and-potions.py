"""
# You are given two positive integer arrays spells and potions, of length
# n and m respectively, where spells[i] represents the strength of the ith
# spell and potions[j] represents the strength of the jth potion.
#
# You are also given an integer success. A spell and potion pair is considered
# successful if the product of their strengths is at least success.
#
# Return an integer array pairs of length n where pairs[i] is the number of
# potions that will form a successful pair with the ith spell.
#
# Constraints:
#    n == spells.length
#    m == potions.length
#    1 <= n, m <= 10^5
#    1 <= spells[i], potions[i] <= 10^5
#    1 <= success <= 10^10
"""

import bisect


class Solution:
    def successfulPairs_pointers(self, spells, potions, success):

    def successfulPairs_bisect(self, spells, potions, success):


def test_solution():
    """test"""

    funcs = [Solution().successfulPairs_pointers, Solution().successfulPairs_bisect]

    data = [
        ([5, 1, 3], [1, 2, 3, 4, 5], 7, [4, 0, 3]),
        ([3, 1, 2], [8, 5, 8], 16, [2, 0, 2]),
    ]

    for spells, potions, success, output in data:
        for func in funcs:
            assert func(spells, potions, success) == output
