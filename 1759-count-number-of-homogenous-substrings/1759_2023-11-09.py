from itertools import groupby


class Solution:
    def countHomogenous_for_loop(self, s):
        result = 1
        streak = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                streak += 1
            else:
                streak = 1
            result += streak

        return result % (1_000_000_007)

    def countHomogenous(self, s):
        result = 0
        for _, group in groupby(s):
            streak = len(list(group))
            result = (result + streak * (streak + 1) // 2) % (10**9 + 7)

        return result


def test_solution():
    """test"""

    funcs = [
        Solution().countHomogenous,
    ]

    # fmt: off
    data = [
        ['abbcccaa', 13],
        ['xy', 2],
        ['zzzzz', 15],
    ]
    # fmt: on

    for func in funcs:
        for s, expected in data:
            assert func(s) == expected
