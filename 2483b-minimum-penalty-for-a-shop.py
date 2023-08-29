"""
You are given the customer visit log of a shop represented by a 0-indexed
string customers consisting only of characters 'N' and 'Y':

    if the ith character is 'Y', it means that customers come at the ith hour

    whereas 'N' indicates that no customers come at the ith hour.

If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated
as follows:

    For every hour when the shop is open and no customers come, the penalty
    increases by 1.

    For every hour when the shop is closed and customers come, the penalty
    increases by 1.

Return the earliest hour at which the shop must be closed to incur a minimum
penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at
the hour j.

Constraints:
    1 <= customers.length <= 10^5
    customers consists only of characters 'Y' and 'N'.
"""


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        return -1


def test_solution():
    """test"""

    funcs = [Solution().bestClosingTime]

    # fmt: off
    data = [
        ['YYNY', 2],
        ['NNNNN', 0],
        ['YYYY', 4],
    ]
    # fmt: on

    for customers, expected in data:
        for func in funcs:
            assert func(customers) == expected


if __name__ == "__main__":
    pass
