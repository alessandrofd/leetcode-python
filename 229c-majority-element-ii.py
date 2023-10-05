"""
Given an integer array of size n, find all elements that appear more than
⌊ n/3 ⌋ times.

Constraints:
    1 <= nums.length <= 5 * 10^4
    -10^9 <= nums[i] <= 10^9
"""

from collections import Counter


class Solution:
    def majorityElement_boyer_moore(self, nums: list[int]) -> list[int]:
        """
        Boyer-Moore Majority Vote

        The algorithm uses O(1) extra space and O(N) time. It requires exactly 2
        passes over the input list. It's also quite simple to implement, though a
        little trickier to understand how it works.

        In the first pass, we generate a single candidate value which is the majority
        value if there is a majority. The second pass simply counts the frequency of
        that value to confirm. The first pass is the interesting part.

        In the first pass, we need 2 values:

        1. A candidate value, initially set to any value.
        2. A count, initially set to 0.

        For each element in our input list, we first examine the count value. If
        the count is equal to 0, we set the candidate to the value at the current
        element. Next, first compare the element's value to the current candidate
        value. If they are the same, we increment count by 1. If they are
        different we decrement count by 1.

        At the end of all of the inputs, the candidate will be the majority value
        if a majority value exists. A second O(N) pass can verify that the
        candidate is the majority element.

        Since the requirement is finding the majority for more than ceiling of
        [n/3], the answer would be less than or equal to two numbers. So we can
        modify the algorithm to maintain two counters for two majorities.
        """

        return []

    def majorityElement_counter(self, nums: list[int]) -> list[int]:
        return []


def test_solution():
    """test"""

    funcs = [
        Solution().majorityElement_boyer_moore,
        Solution().majorityElement_counter,
    ]

    # fmt: off
    data = [
        [[3,2,3], [3]],
        [[1], [1]],
        [[1,2], [1,2]],
        [[2,2], [2]],
        [[0,0,0], [0]],
        [[4,1,2,3,4,4,3,2,1,4], [4]]
    ]
    # fmt: on
    for nums, expected in data:
        for func in funcs:
            assert func(nums) == expected
