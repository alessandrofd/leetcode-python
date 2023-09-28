"""
Given an integer array nums, move all the even integers at the beginning of
the array followed by all the odd integers.

Return any array that satisfies this condition.

Constraints:
    1 <= nums.length <= 5000
    0 <= nums[i] <= 5000
"""


class Solution:
    def sortArrayByParity_swap(self, nums: list[int]) -> list[int]:
        return nums

    def sortArrayByParity_sort(self, nums: list[int]) -> list[int]:
        return nums


def test_solution():
    """test"""

    funcs = [
        Solution().sortArrayByParity_swap,
        Solution().sortArrayByParity_sort,
    ]

    # fmt: off
    data = [
        [[3, 1, 2, 4], [2, 4, 3, 1]],
        [[0], [0]],
    ]
    # fmt: on

    for nums, expected in data:
        for func in funcs:
            assert func(nums) == expected


if __name__ == "__main__":
    pass
