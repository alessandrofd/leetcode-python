"""
There are n children standing in a line. Each child is assigned a rating
value given in the integer array ratings.

You are giving candies to these children subjected to the following
requirements:

    Each child must have at least one candy.

    Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the
candies to the children.

Constraints:
    n == ratings.length
    1 <= n <= 2 * 10^4
    0 <= ratings[i] <= 2 * 10^4
"""


from typing import List


class Solution:
    def candy_brute_force(self, ratings: List[int]) -> int:
        return 0

    def candy_two_arrays(self, ratings: List[int]) -> int:
        return 0

    def candy_single_array(self, ratings: List[int]) -> int:
        return 0

    def candy_single_pass(self, ratings: List[int]) -> int:
        return 0


def test_solution():
    """test"""

    # fmt: off
    funcs = [
        Solution().candy_brute_force,
        Solution().candy_two_arrays,
        Solution().candy_single_array,
        Solution().candy_single_pass,
    ]

    data = [
        [[1, 0, 2], 5],
        [[1, 2, 2], 4],
    ]
    # fmt: on

    for ratings, expected in data:
        for func in funcs:
            assert func(ratings) == expected


if __name__ == "__main__":
    pass
