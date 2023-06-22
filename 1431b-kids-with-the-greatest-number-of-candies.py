"""
There are n kids with candies. You are given an integer array candies, where
each candies[i] represents the number of candies the ith kid has, and
an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is True if, after
giving the ith kid all the extraCandies, they will have the greatest number
of candies among all the kids, or False otherwise.

Note that multiple kids can have the greatest number of candies.

Constraints:
    n == candies.length
    2 <= n <= 100
    1 <= candies[i] <= 100
    1 <= extraCandies <= 50
"""


class Solution:
    def kidsWithCandies_sort(self, candies, extra_candies):
        pass

    def kidsWithCandies_max(self, candies, extra_candies):
        pass


def test_solution():
    """test"""

    funcs = [
        Solution().kidsWithCandies_sort,
        Solution().kidsWithCandies_max,
    ]

    data = [
        ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
        ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
        ([12, 1, 12], 10, [True, False, True]),
    ]

    for candies, extra_candies, output in data:
        for func in funcs:
            assert func(candies, extra_candies) == output
