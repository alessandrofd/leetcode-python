"""
You have a long flowerbed in which some of the plots are planted, and some
are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty
and 1 means not empty, and an integer n, return if n new flowers can be
planted in the flowerbed without violating the no-adjacent-flowers rule.

Constraints:
    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
"""

from typing import List


class Solution:
    """Solution class"""

    def canPlaceFlowers(self, flowerbed: List[int], new_flowers: int) -> bool:
        """Solution func"""

        return True


def test_detectCycle():
    """test"""

    funcs = [Solution().canPlaceFlowers]

    data = [
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([1, 0, 0, 0, 1, 0, 0], 2, True),
        ([0, 0], 2, False),
        ([0], 1, True),
    ]

    for flowerbed, new_flowers, output in data:
        for func in funcs:
            assert func(flowerbed, new_flowers) == output
