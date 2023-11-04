class Solution:
    def getLastMoment(self, n, left, right):
        result = 0
        if left:
            result = max(left)
        if right:
            result = max(result, n - min(right))
        return result


def test_solution():
    """test"""

    funcs = [
        Solution().getLastMoment,
    ]

    # fmt: off
    data = [
        [4, [4, 3], [0, 1], 4],
        [7, [], [0, 1, 2, 3, 4, 5, 6, 7], 7],
        [7, [0, 1, 2, 3, 4, 5, 6, 7], [], 7],
    ]
    # fmt: on

    for func in funcs:
        for n, left, right, expected in data:
            assert func(n, left, right) == expected
