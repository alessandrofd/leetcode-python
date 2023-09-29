"""
An array is monotonic if it is either monotone increasing or monotone
decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or
false otherwise.

Constraints:
    1 <= nums.length <= 10^5
    -10^5 <= nums[i] <= 10^5
"""


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        return True


def test_solution():
    """test"""

    # fmt: off
    funcs = [
        Solution().isMonotonic,
    ]

    data = [
        [[1, 2, 2, 3], True],
        [[6, 5, 4, 4], True],
        [[1, 3, 2], False],
    ]
    # fmt: on

    for nums, expected in data:
        for func in funcs:
            assert func(nums) == expected


if __name__ == "__main__":
    pass
