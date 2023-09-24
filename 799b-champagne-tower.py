"""
We stack glasses in a pyramid, where the first row has 1 glass, the second
row has 2 glasses, and so on until the 100th row.  Each glass holds one cup
of champagne.

Then, some champagne is poured into the first glass at the top.  When the
topmost glass is full, any excess liquid poured will fall equally to the
glass immediately to the left and right of it.  When those glasses become
full, any excess champagne will fall equally to the left and right of those
glasses, and so on.  (A glass at the bottom row has its excess champagne fall
on the floor.)

For example, after one cup of champagne is poured, the top most glass is
full.  After two cups of champagne are poured, the two glasses on the second
row are half full.  After three cups of champagne are poured, those two cups
become full - there are 3 full glasses total now.  After four cups of
champagne are poured, the third row has the middle glass half full, and the
two outside glasses are a quarter full, as pictured below.

Now after pouring some non-negative integer cups of champagne, return how
full the jth glass in the ith row is (both i and j are 0-indexed.)

Constraints:
    0 <= poured <= 10^9
    0 <= query_glass <= query_row < 100
"""


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        Simulation

        Instead of keeping track of how much champagne should end up in a glass,
        keep track of the total amount of champagne that flows through a glass.
        For example, if poured = 10 cups are poured at the top, then the total
        flow-through of the top glass is 10; the total flow-through of each
        glass in the second row is 4.5, and so on.

        In general, if a glass has flow-through X, then Q = (X - 1.0) / 2.0
        quantity of champagne will equally flow left and right. We can simulate
        the entire pour for 100 rows of glasses. A glass at (r, c) will have
        excess champagne flow towards (r+1, c) and (r+1, c+1).
        """
        return 0.0


def test_solution():
    """test"""

    funcs = [
        Solution().champagneTower,
    ]

    # fmt: off
    data = [
        [1, 1, 1, 0.0],
        [2, 1, 1, 0.5],
        [100000009, 33, 17, 1.0],
        [1000000000, 99, 99, 0.0],
    ]
    # fmt: on

    for poured, query_row, query_glass, expected in data:
        for func in funcs:
            assert func(poured, query_row, query_glass) == expected


if __name__ == "__main__":
    pass
