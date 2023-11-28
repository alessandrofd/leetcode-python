class Solution:
    def knightDialer(self, length):
        if length == 1:
            return 10

        mod = 10**9 + 7

        A, B, C, D = 4, 2, 2, 1
        for _ in range(1, length):
            A, B, C, D = (2 * (B + C)) % mod, A, (A + 2 * D) % mod, C

        return (A + B + C + D) % mod

    def knightDialer_dp_bottom_up_optimized(self, length):
        mod = 10**9 + 7
        graph = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4],
        ]

        previous = [1] * 10

        for _ in range(1, length):
            current = [0] * 10
            for j in range(10):
                current[j] = sum(previous[k] for k in graph[j]) % mod
            previous = current

        return sum(previous) % mod

    def knightDialer_dp_bottom_up(self, length):
        mod = 10**9 + 7
        graph = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4],
        ]

        dp = [[1] * 10 for _ in range(length)]

        for i in range(1, length):
            for j in range(10):
                dp[i][j] = sum(dp[i - 1][k] for k in graph[j]) % mod

        return sum(dp[-1]) % mod


def test_solution():
    """test solution"""

    funcs = [
        Solution().knightDialer,
        Solution().knightDialer_dp_bottom_up_optimized,
        Solution().knightDialer_dp_bottom_up,
    ]

    data = [
        [1, 10],
        [2, 20],
        [3131, 136006598],
    ]

    for func in funcs:
        for length, expected in data:
            assert func(length) == expected
