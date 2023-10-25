class Solution:
    def kthGrammar_bin_search(self, n: int, k: int) -> int:
        def dfs(n, k, root):
            if n == 1:
                return root

            mid = 2 ** (n - 1) / 2
            if k > mid:
                root = 1 - root
                k -= mid

            return dfs(n - 1, k, root)

        return dfs(n, k, 0)

    def kthGrammar_recursion(self, n: int, k: int) -> int:
        def recurse(n, k):
            if n == 1:
                return 0

            mid = 2 ** (n - 1) / 2
            if k > mid:
                return 1 - recurse(n, k - mid)

            return recurse(n - 1, k)

        return recurse(n, k)

    def kthGrammar_iteration(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        flips = 0
        for row in range(n, 1, -1):
            mid = 2 ** (row - 1) / 2
            if k > mid:
                flips += 1
                k -= mid

        return 1 if flips % 2 else 0

    def kthGrammar_math(self, n: int, k: int) -> int:
        return 1 if (k - 1).bit_count() % 2 else 0

    def kthGrammar_doubling(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        if k % 2:
            return self.kthGrammar_doubling(n - 1, (k + 1) // 2)

        return 1 - self.kthGrammar_doubling(n - 1, k // 2)


def test_solution():
    """test"""

    funcs = [
        Solution().kthGrammar_bin_search,
        Solution().kthGrammar_recursion,
        Solution().kthGrammar_iteration,
        Solution().kthGrammar_math,
        Solution().kthGrammar_doubling,
    ]

    # fmt: off
    data = [
        [1, 1, 0],
        [2, 1, 0],
        [2, 2, 1],
    ]
    # fmt: on

    for func in funcs:
        for n, k, expected in data:
            assert func(n, k) == expected
