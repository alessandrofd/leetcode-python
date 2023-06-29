"""
You are given an m x n grid grid where:

    '.' is an empty cell.
    '#' is a wall.
    '@' is the starting point.
    Lowercase letters represent keys.
    Uppercase letters represent locks.

You start at the starting point and one move consists of walking one space in
one of the four cardinal directions. You cannot walk outside the grid,
or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock
unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter
of the first k letters of the English alphabet in the grid. This means that
there is exactly one key for each lock, and one lock for each key; and also
that the letters used to represent the keys and locks were chosen in the same
order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible,
return -1.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 30
    grid[i][j] is either an English letter, '.', '#', or '@'.
    The number of keys in the grid is in the range [1, 6].
    Each key in the grid is unique.
    Each key in the grid has a matching lock.
"""

## BFS. O pulo do gato é que cada vez que encontramos uma chave temos que zerar
## as células visitadas

from typing import List
from itertools import product
from collections import deque, defaultdict


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        return -1


def test_solution():
    """test"""

    funcs = [
        Solution().shortestPathAllKeys,
    ]

    # fmt: off
    data = [
        (['@.a..', '###.#', 'b.A.B'], 8),
        (['@..aA', '..B#.', '....b'], 6),
        (['@Aa'], -1),
    ]
    # fmt: on
    for grid, expected in data:
        for func in funcs:
            assert func(grid) == expected
