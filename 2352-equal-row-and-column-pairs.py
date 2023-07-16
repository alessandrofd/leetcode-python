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
        n = len(grid)
        transposed = list(zip(*grid))

        result = 0
        for i, j in product(range(n), repeat=2):
            if tuple(grid[i]) == transposed[j]:
                result += 1

        return result

    def equalPairs_hash(self, grid: List[List[int]]) -> int:
        count_rows = Counter(tuple(row) for row in grid)

        transposed = list(zip(*grid))
        return sum(count_rows[col] for col in transposed)

    def equalPairs_trie(self, grid: List[List[int]]) -> int:
        class TrieNode:
            def __init__(self):
                self.count = 0
                self.children = {}

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def insert(self, nums):
                trie = self.root
                for num in nums:
                    if num not in trie.children:
                        trie.children[num] = TrieNode()
                    trie = trie.children[num]
                trie.count += 1

            def search(self, nums):
                trie = self.root
                for num in nums:
                    if num in trie.children:
                        trie = trie.children[num]
                    else:
                        return 0
                return trie.count

        trie = Trie()
        for row in grid:
            trie.insert(row)

        transposed = list(zip(*grid))
        return sum(trie.search(col) for col in transposed)


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
