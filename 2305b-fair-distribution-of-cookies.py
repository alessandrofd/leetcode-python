"""
You are given an integer array cookies, where cookies[i] denotes the number
of cookies in the ith bag. You are also given an integer k that denotes
the number of children to distribute all the bags of cookies to. All
the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies
obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.

Constraints:
    2 <= cookies.length <= 8
    1 <= cookies[i] <= 10^5
    2 <= k <= cookies.length
"""

# Backtracking otimizado considerando que a quantidade de sacos de biscoitos
# sempre será maior ou igual à quantidade de crianças


from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], num_children: int) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().distributeCookies,
    ]

    # fmt: off
    data = [
        ([8, 15, 10, 20, 8], 2, 31),
        ([6, 1, 3, 2, 2, 4, 1, 2], 3, 7),
    ]
    # fmt: on
    for cookies, k, expected in data:
        for func in funcs:
            assert func(cookies, k) == expected
