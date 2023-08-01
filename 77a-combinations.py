"""
Given two integers n and k, return all possible combinations of k numbers
chosen from the range [1, n].

You may return the answer in any order.

Constraints:
    1 <= n <= 20
    1 <= k <= n
"""
from typing import List
from itertools import combinations


class Solution:
    def combine_backtrack(self, n: int, k: int) -> List[List[int]]:
        return [[0]]

    def combine_builtin(self, n: int, k: int) -> List[tuple[int]]:
        return


def test_solution():
    """test"""

    funcs = [
        Solution().combine_backtrack,
        Solution().combine_builtin,
    ]

    # fmt: off
    data = [
        (4, 2, [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]),
        (1, 1, [[1]]),
    ]
    # fmt: on
    for n, k, expected in data:
        for func in funcs:
            assert func(n, k).sort() == expected.sort()


if __name__ == "__main__":
    pass
