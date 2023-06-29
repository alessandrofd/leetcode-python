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
        m, n = len(grid), len(grid[0])

        def to_bitmap(cell: str) -> int:
            return 1 << ((ord(cell) & 31) - 1)

        def is_locked(cell: str, keys: int) -> bool:
            return cell in "ABCDEF" and not to_bitmap(cell) & keys

        moves = ((-1, 0), (0, 1), (1, 0), (0, -1))

        queue = deque()
        count_keys = 0
        for row, col in product(range(m), range(n)):
            cell = grid[row][col]
            if cell == "@":
                queue.append((row, col, 0, 0))
            elif cell in "abcdef":
                count_keys += 1

        all_keys = (2**count_keys) - 1
        visited = defaultdict(set)

        while queue:
            row, col, keys, distance = queue.popleft()

            if row < 0 or row >= m or col < 0 or col >= n:
                continue

            cell = grid[row][col]

            if cell == "#" or (row, col) in visited[keys]:
                continue

            visited[keys].add((row, col))

            if is_locked(cell, keys):
                continue

            if cell in "abcdef":
                keys |= to_bitmap(cell)

            if all_keys == keys:
                return distance

            for move_row, move_col in moves:
                queue.append((row + move_row, col + move_col, keys, distance + 1))

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
