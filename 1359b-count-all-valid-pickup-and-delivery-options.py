"""
Given n orders, each order consist in pickup and delivery services.

Count all valid pickup/delivery possible sequences such that delivery(i) is
always after of pickup(i).

Since the answer may be too large, return it modulo 10^9 + 7.

Constraints:
    1 <= n <= 500
"""


class Solution:
    def countOrders_bottom_up(self, num_orders):
        """
        Assume we have already n - 1 pairs, now we need to insert the nth pair.
        To insert the first element, there are n * 2 - 1 choices of position.
        To insert the second element, there are n * 2 chioces of position。
        So there are (n * 2 - 1) * n * 2 permutations.
        Considering that delivery(i) is always after of pickup(i), we need to
        divide by 2.
        So it's (n * 2 - 1) * n.
        """
        return 0

    def countOrders_top_down(self, num_orders):
        """
        Mesma lógica da solução anterior
        """
        return 0


def test_solution():
    """test"""

    # fmt: off
    funcs = [
        Solution().countOrders_top_down,
        Solution().countOrders_bottom_up,
    ]

    data = [
        [1, 1],
        [2, 6],
        [3, 90],
        [7, 681080400],
    ]
    # fmt: on

    for num_orders, expected in data:
        for func in funcs:
            assert func(num_orders) == expected


if __name__ == "__main__":
    pass
