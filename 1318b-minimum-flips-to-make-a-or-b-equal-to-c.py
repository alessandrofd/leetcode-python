"""
Given 3 positives numbers a, b and c. Return the minimum flips required in
some bits of a and b to make ( a OR b == c ). (bitwise OR operation).

Flip operation consists of change any single bit 1 to 0 or change
the bit 0 to 1 in their binary representation.

Constraints:
    1 <= a <= 10^9
    1 <= b <= 10^9
    1 <= c <= 10^9
"""


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().minFlips,
    ]

    # fmt: off
    data = [
        (2, 6, 5, 3),
        (4, 2, 7, 1),
        (1, 2, 3, 0),
        (8, 3, 5, 3),
        (5, 2, 8, 4),
    ]
    # fmt: on
    for a, b, c, expected in data:
        for func in funcs:
            assert func(a, b, c) == expected
