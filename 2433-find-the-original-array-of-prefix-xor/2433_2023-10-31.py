class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        n = len(pref)

        arr = [0] * n
        arr[0] = pref[0]

        for i in range(1, n):
            arr[i] = pref[i] ^ pref[i - 1]
        return arr

    def findArray_space_optimized(self, pref: list[int]) -> list[int]:
        n = len(pref)

        for i in range(n - 1, 0, -1):
            pref[i] ^= pref[i - 1]
        return pref


def test_solution():
    """test"""

    funcs = [
        Solution().findArray,
    ]

    # fmt: off
    data = [
        [[5,2,0,3,1], [5,7,2,3,2]],
        [[13], [13]],
    ]
    # fmt: on

    for func in funcs:
        for pref, expected in data:
            assert func(pref) == expected
