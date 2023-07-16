"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs
(ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements
in the same order (i.e., an equal array).

Constraints:
    n == grid.length == grid[i].length
    1 <= n <= 200
    1 <= grid[i][j] <= 10^5
"""


from typing import List
from itertools import product
from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        return 0

    def equalPairs_hash(self, grid: List[List[int]]) -> int:
        return 0

    def equalPairs_trie(self, grid: List[List[int]]) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().equalPairs,
        Solution().equalPairs_hash,
        Solution().equalPairs_trie,
    ]

    # fmt: off
    data = [
        ([[3,2,1],[1,7,6],[2,7,7]], 1), 
        ([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]], 3),
    ]
    # fmt: on
    for grid, expected in data:
        for func in funcs:
            assert func(grid) == expected
