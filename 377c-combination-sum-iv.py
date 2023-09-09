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


class Solution:
    def combinationSum4_dp_top_down(self, nums, target):
        """DP Top-Down"""
        pass

    def combinationSum4_dp_bottom_up(self, nums, target):
        """DP Bottom-Up"""
        pass

    def combinationSum4_dp_bottom_up_optimized(self, nums, target):
        """DP Bottom-Up Optimized"""
        pass


def test_solution():
    """test"""

    # fmt: off
    funcs = [
        Solution().combinationSum4_dp_top_down,
        Solution().combinationSum4_dp_bottom_up,
        Solution().combinationSum4_dp_bottom_up_optimized,
    ]

    data = [
    [[1, 2, 3], 4, 7],
    [[9], 3, 0],
    ]
    # fmt: on

    for nums, target, expected in data:
        for func in funcs:
            assert func(nums, target) == expected


if __name__ == "__main__":
    pass
