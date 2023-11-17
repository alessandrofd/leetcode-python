class Solution:
    def minPairSum(self, nums):
        n = len(nums)
        nums.sort()

        result = 0
        for i in range(n // 2):
            result = max(result, nums[i] + nums[-1 - i])

        return result


def test_solution():
    """test"""

    funcs = [
        Solution().minPairSum,
    ]

    data = [
        [[3, 5, 2, 3], 7],
        [[3, 5, 4, 2, 4, 6], 8],
    ]

    for func in funcs:
        for nums, expected in data:
            assert func(nums) == expected
