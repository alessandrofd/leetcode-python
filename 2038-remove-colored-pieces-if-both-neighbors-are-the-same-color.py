"""
There are n pieces arranged in a line, and each piece is colored either by
'A' or by 'B'. You are given a string colors of length n where colors[i] is
the color of the ith piece.

Alice and Bob are playing a game where they take alternating turns removing
pieces from the line. In this game, Alice moves first.

    Alice is only allowed to remove a piece colored 'A' if both its neighbors
    are also colored 'A'. She is not allowed to remove pieces that are colored
    'B'.

    Bob is only allowed to remove a piece colored 'B' if both its neighbors
    are also colored 'B'. He is not allowed to remove pieces that are colored
    'A'.

    Alice and Bob cannot remove pieces from the edge of the line.

    If a player cannot make a move on their turn, that player loses and the
    other player wins.

Assuming Alice and Bob play optimally, return true if Alice wins, or return
false if Bob wins.

Constraints:
    1 <= colors.length <= 10^5
    colors consists of only the letters 'A' and 'B'
"""


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        if n < 3:
            return False

        alice, bob = 0, 0
        for i in range(2, n):
            if colors[i] == colors[i - 1] == colors[i - 2]:
                if colors[i] == "A":
                    alice += 1
                else:
                    bob += 1

        return alice >= bob + 1


def test_solution():
    """test"""

    funcs = [
        Solution().winnerOfGame,
    ]

    # fmt: off
    data = [
        ['AAABABB', True],
        ['AA', False],
        ['ABBBBBBBAAA', False],
    ]
    # fmt: on
    for colors, expected in data:
        for func in funcs:
            assert func(colors) == expected
