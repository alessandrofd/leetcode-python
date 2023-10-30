class Solution:
    def sortByBits_builtin(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda num: (num.bit_count(), num))

    def sortByBits_bit_manipulation(self, arr: list[int]) -> list[int]:
        def find_weight(num):
            weight = 0
            mask = 1
            while num:
                if num & mask:
                    weight += 1
                    num ^= mask
                mask <<= 1
            return weight

        return sorted(arr, key=lambda num: (find_weight(num), num))

    def sortByBits_kerningham(self, arr: list[int]) -> list[int]:
        def find_weight(num):
            weight = 0
            while num:
                weight += 1
                num &= num - 1
            return weight

        return sorted(arr, key=lambda num: (find_weight(num), num))


def test_solution():
    """test"""

    funcs = [
        Solution().sortByBits_builtin,
        Solution().sortByBits_bit_manipulation,
        Solution().sortByBits_kerningham,
    ]

    # fmt: off
    data = [
        [
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
            [0, 1, 2, 4, 8, 3, 5, 6, 7],
        ],
        [
            [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 0],
            [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],
        ],
    ]
    # fmt: on

    for func in funcs:
        for s, expected in data:
            assert func(s) == expected
