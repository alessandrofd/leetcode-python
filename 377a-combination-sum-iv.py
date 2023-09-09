"""
Given an array of distinct integers nums and a target integer target, return
the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

Constraints:
    1 <= nums.length <= 200
    1 <= nums[i] <= 1000
    All the elements of nums are unique.
    1 <= target <= 1000
"""

from functools import cache


class Solution:
    def combinationSum4_dp_top_down(self, nums, target):
        """DP Top-Down"""

        @cache
        def dfs(comb_sum):
            if comb_sum == target:
                return 1
            if comb_sum > target:
                return 0

            result = 0
            for num in nums:
                result += dfs(comb_sum + num)

            return result

        return dfs(0)

    def combinationSum4_dp_bottom_up(self, nums, target):
        """DP Bottom-Up"""

        dp = [0] * (target + 1)
        dp[target] = 1

        for i in range(target - 1, -1, -1):
            for num in nums:
                if i + num <= target:
                    dp[i] += dp[i + num]

        return dp[0]

    def combinationSum4_dp_bottom_up_optimized(self, nums, target):
        """DP Bottom-Up Optimized"""

        sorted_nums = sorted(nums)
        dp = [0] * (target + 1)
        dp[target] = 1

        for i in range(target - 1, -1, -1):
            for num in sorted_nums:
                if i + num <= target:
                    dp[i] += dp[i + num]
                else:
                    break

        return dp[0]


def test_solution():
    """test"""

    # fmt: off
    funcs = [
        Solution().combinationSum4_dp_top_down,
        Solution().combinationSum4_dp_bottom_up,
        Solution().combinationSum4_dp_bottom_up_optimized,
    ]

    data = [
    [[3, 2, 1], 4, 7],
    [[9], 3, 0],
    ]
    # fmt: on

    for nums, target, expected in data:
        for func in funcs:
            assert func(nums, target) == expected


if __name__ == "__main__":
    pass
