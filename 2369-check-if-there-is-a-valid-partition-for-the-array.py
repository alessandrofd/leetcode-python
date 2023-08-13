"""
You are given a 0-indexed integer array nums. You have to partition the array
into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays
satisfies one of the following conditions:

    1.  The subarray consists of exactly 2 equal elements.
        For example, the subarray [2,2] is good.

    2.  The subarray consists of exactly 3 equal elements.
        For example, the subarray [4,4,4] is good.

    3.  The subarray consists of exactly 3 consecutive increasing elements,
        that is, the difference between adjacent elements is 1.
        For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is
        not.

Return true if the array has at least one valid partition. Otherwise, return
false.

Constraints:
    2 <= nums.length <= 10^5
    1 <= nums[i] <= 10^6
"""

from typing import List


class Solution:
    def validPartition_bottom_up_dp(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[1] = nums[1] == nums[0]
        if n > 2:
            dp[2] = (
                nums[2] == nums[1] == nums[0] or nums[2] == nums[1] + 1 == nums[0] + 2
            )

        for i in range(3, n):
            if nums[i] == nums[i - 1]:
                dp[i] = dp[i] or dp[i - 2]
            if (
                nums[i] == nums[i - 1] == nums[i - 2]
                or nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2
            ):
                dp[i] = dp[i] or dp[i - 3]

        return dp[-1]

    def validPartition_bottom_up_dp_optimized(self, nums: List[int]) -> bool:
        last = True
        previous = False
        current = nums[1] == nums[0]

        for i in range(2, len(nums)):
            last, previous, current = (
                previous,
                current,
                (previous and nums[i] == nums[i - 1])
                or (
                    last
                    and (
                        nums[i] == nums[i - 1] == nums[i - 2]
                        or nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2
                    )
                ),
            )

        return current


def test_solution():
    """test"""

    funcs = [
        Solution().validPartition_bottom_up_dp,
        Solution().validPartition_bottom_up_dp_optimized,
    ]

    # fmt: off
    data = [
        ([4, 4, 4, 5, 6], True),
        ([1, 1, 1, 2], False),
        ([1,2], False),
        ([ 579611, 579611, 579611, 731172, 731172, 496074, 496074, 496074, 151416, 151416, 151416, ], True),
    ]
    # fmt: on
    for nums, expected in data:
        for func in funcs:
            assert func(nums) == expected


if __name__ == "__main__":
    pass
