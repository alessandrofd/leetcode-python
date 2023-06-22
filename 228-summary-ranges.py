"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the
array exactly. That is, each element of nums is covered by exactly one of the
ranges, and there is no integer x such that x is in one of the ranges but not
in nums.

Each range [a,b] in the list should be output as:
    "a->b" if a != b
    "a" if a == b

Constraints:
    0 <= nums.length <= 20
    -2^31 <= nums[i] <= 2^31 - 1
    All the values of nums are unique.
    nums is sorted in ascending order.
"""

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        if not nums:
            return result

        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if nums[i - 1] == start:
                    result.append(str(nums[i - 1]))
                else:
                    result.append(f"{start}->{nums[i-1]}")
                start = nums[i]

        if nums[-1] == start:
            result.append(str(nums[-1]))
        else:
            result.append(f"{start}->{nums[-1]}")

        return result


def test_solution():
    """test"""

    funcs = [
        Solution().summaryRanges,
    ]

    data = [
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
        ([], []),
    ]
    for nums, expected in data:
        for func in funcs:
            assert func(nums) == expected
