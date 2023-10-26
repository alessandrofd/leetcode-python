from math import isqrt


class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        n = len(arr)
        MOD = int(1e9 + 7)

        arr.sort()
        trees_by_root = {}

        result = 0
        for i in range(n):
            root = arr[i]
            trees = 1
            lim = isqrt(root)
            j = 0
            while arr[j] <= lim:
                left = arr[j]
                right = arr[i] / arr[j]
                if right in trees_by_root:
                    trees = (
                        trees
                        + trees_by_root[left]
                        * trees_by_root[right]
                        * (1 if left == right else 2)
                    ) % MOD

                j += 1

            trees_by_root[root] = trees
            result = (result + trees) % MOD

        return result


def test_solution():
    """test"""

    funcs = [
        Solution().numFactoredBinaryTrees,
    ]

    # fmt: off
    data = [
        [[2, 4], 3],
        [[2, 4, 5, 10], 7],
    ]
    # fmt: on

    for func in funcs:
        for arr, expected in data:
            assert func(arr) == expected
