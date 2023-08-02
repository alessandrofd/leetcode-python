"""
Given an array nums of distinct integers, return all the possible
permutations. You can return the answer in any order.

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
"""

from typing import List
from itertools import permutations


class Solution:
    def permute_backtrack(self, nums: List[int]) -> List[List[int]]:
        return [[0]]

    def permute_builtin(self, nums: List[int]) -> List[tuple[int]]:
        return


def test_solution():
    """test"""

    funcs = [
        Solution().permute_backtrack,
        Solution().permute_builtin,
    ]

    # fmt: off
    data = [
        ([1, 2, 3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
        ([0, 1], [[0,1],[1,0]]),
        ([1], [[1]]),
    ]
    # fmt: on
    for permute, expected in data:
        for func in funcs:
            assert func(permute).sort() == expected.sort()


if __name__ == "__main__":
    pass
