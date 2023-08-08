"""
There is an integer array nums sorted in ascending order (with distinct
values).

Prior to being passed to your function, nums is possibly rotated at an
unknown pivot index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
(0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
    1 <= nums.length <= 5000
    -10^4 <= nums[i] <= 10^4
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -10^4 <= target <= 10^4
"""

from typing import List


class Solution:
    def search_1loop(self, nums: List[int], target: int) -> int:
        return -1

    def search_2loops(self, nums: List[int], target: int) -> int:
        """
        Na busca binária temos que decidir qual metade do vetor está ordenada. Se o
        valor procurado estiver na metade ordenada, procedemos com a busca nesta
        metade, caso contrário na outra. A decisão só pode ser tomada avaliando a
        metade ordenada.
        """
        return -1


def test_solution():
    """test"""

    funcs = [
        Solution().search_1loop,
        Solution().search_2loops,
    ]

    # fmt: off
    data = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([1, 3], 3, 1),
    ]
    # fmt: on
    for nums, target, expected in data:
        for func in funcs:
            assert func(nums, target) == expected


if __name__ == "__main__":
    pass
