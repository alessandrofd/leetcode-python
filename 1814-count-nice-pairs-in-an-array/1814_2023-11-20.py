from collections import defaultdict, Counter


class Solution:
    def countNicePairs(self, nums):
        # def reverse(num):
        #     result = 0
        #     while num:
        #         modulo = num % 10
        #         result = result * 10 + modulo
        #         num = (num - modulo) // 10

        #     return result

        def reverse(num):
            return int(str(num)[::-1])

        diffs = defaultdict(int)
        for num in nums:
            diffs[num - reverse(num)] += 1

        result = 0
        for count in diffs.values():
            result += count * (count - 1) / 2

        return int(result % (1e9 + 7))


def test_solution():
    """test"""

    # fmt: on
    funcs = [
        Solution().countNicePairs,
    ]

    data = [
        [[42, 11, 1, 97], 2],
        [[13, 10, 35, 24, 76], 4],
    ]
    # fmt: off

    for func in funcs:
        for nums, expected in data:
            assert func(nums) == expected
