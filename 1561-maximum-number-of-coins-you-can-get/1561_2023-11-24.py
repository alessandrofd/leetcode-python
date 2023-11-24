class Solution:
    def maxCoins(self, piles):
        return sum(sorted(piles)[len(piles) // 3 :: 2])

    def maxCoins_sort_standard(self, piles):
        piles.sort()
        n = len(piles)
        res = 0
        for i in range(n // 3, n, 2):
            res += piles[i]
        return res


def test_solution():
    """test"""

    funcs = [
        Solution().maxCoins,
        Solution().maxCoins_sort_standard,
    ]

    datas = [
        [[2, 4, 1, 2, 7, 8], 9],
        [[2, 4, 5], 4],
        [[9, 8, 7, 6, 5, 1, 2, 3, 4], 18],
    ]

    for f in funcs:
        for piles, expected in datas:
            assert f(piles) == expected
