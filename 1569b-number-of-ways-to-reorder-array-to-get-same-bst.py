"""
Given an array nums that represents a permutation of integers from 1 to n.
We are going to construct a binary search tree (BST) by inserting the
elements of nums in order into an initially empty BST. Find the number of
different ways to reorder nums so that the constructed BST is identical to
that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left
child, and 3 as a right child. The array [2,3,1] also yields the same BST but
[3,2,1] yields a different BST.

Return the number of ways to reorder nums such that the BST formed is
identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 10^9 + 7.

Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= nums.length
    All integers in nums are distinct.
"""
from typing import List
from math import comb


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().numOfWays,
    ]

    # fmt: off
    data = [
        ([2, 1, 3], 1),
        ([3, 4, 5, 1, 2], 5),
        ([1, 2, 3], 0),
        ([10, 23, 12, 18, 4, 29, 2, 8, 41, 31, 25, 21, 14, 35, 26, 5, 19, 43, 22, 
          37, 9, 20, 44, 28, 1, 39, 30, 38, 36, 6, 13, 16, 27, 17, 34, 7, 15, 3, 
          11, 24, 42, 33, 40, 32], 182440977,
        ),
    ]
    # fmt: on
    for nums, expected in data:
        for func in funcs:
            assert func(nums) == expected
