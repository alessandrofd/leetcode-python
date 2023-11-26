from itertools import accumulate


class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)

        total_sum = sum(nums)
        left_sum = 0

        result = [0] * n
        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num
            result[i] = (i * num - left_sum) + (right_sum - (n - i - 1) * num)

            left_sum += num

        return result

    def getSumAbsoluteDifferences_prefix_sum(self, nums):
        n = len(nums)

        prefix_sum = list(accumulate(nums))

        result = []
        for i, num in enumerate(nums):
            left_sum = (i + 1) * num - prefix_sum[i]
            right_sum = prefix_sum[-1] - prefix_sum[i] - (n - i - 1) * num
            result.append(left_sum + right_sum)

        return result


def test_solution():
    """test solution"""

    funcs = [
        Solution().getSumAbsoluteDifferences,
        Solution().getSumAbsoluteDifferences_prefix_sum,
    ]

    data = [
        [
            [2, 3, 5],
            [4, 3, 5],
        ],
        [
            [1, 4, 6, 8, 10],
            [24, 15, 13, 15, 21],
        ],
    ]

    for func in funcs:
        for nums, expected in data:
            assert func(nums) == expected
