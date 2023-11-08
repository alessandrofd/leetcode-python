class Solution:
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        width = abs(sx - fx)
        height = abs(sy - fy)
        min_time = max(width, height)

        if min_time == 0 and t == 1:
            return False

        return min_time <= t


def test_solution():
    """test"""

    funcs = [
        Solution().isReachableAtTime,
    ]

    # fmt: off
    data = [
        [2, 4, 7, 7, 6, True],
        [3, 1, 7, 3, 3, False],
    ]
    # fmt: on

    for func in funcs:
        for sx, sy, fx, fy, t, expected in data:
            assert func(sx, sy, fx, fy, t) == expected
