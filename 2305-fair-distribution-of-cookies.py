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
        MAX_UNFAIRNESS = 8 * 10**5
        num_cookies = len(cookies)
        distribution = [0] * num_children

        def backtrack(curr_cookie: int, zeroes: int) -> int:
            if curr_cookie == num_cookies:
                return max(distribution)
            if zeroes > num_cookies - curr_cookie:
                return MAX_UNFAIRNESS

            unfairness = MAX_UNFAIRNESS

            for curr_child in range(num_children):
                if distribution[curr_child] + cookies[curr_cookie] > unfairness:
                    continue
                if (
                    curr_child > 0
                    and distribution[curr_child] == distribution[curr_child - 1]
                ):
                    continue

                zeroes -= 1 if distribution[curr_child] == 0 else 0
                distribution[curr_child] += cookies[curr_cookie]

                unfairness = min(unfairness, backtrack(curr_cookie + 1, zeroes))

                distribution[curr_child] -= cookies[curr_cookie]
                zeroes += 1 if distribution[curr_child] == 0 else 0

            return unfairness

        return backtrack(0, num_children)


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
