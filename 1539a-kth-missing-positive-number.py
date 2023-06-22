"""
Given an array arr of positive integers sorted in a strictly increasing
order, and an integer k.
Return the kth positive integer that is missing from this array.
Constraints:
    1 <= arr.length <= 1000
    1 <= arr[i] <= 1000
    1 <= k <= 1000
    arr[i] < arr[j] for 1 <= i < j <= arr.length
"""

from typing import List


class Solution:
    """Solution class"""

    def findKthPositive_brute(  # pylint: disable=invalid-name
        self, arr: List[int], k: int
    ) -> int:
        """Brute force"""

    def findKthPositive_binSearch(  # pylint: disable=invalid-name
        self, arr: List[int], k: int
    ) -> int:
        """Binary Search"""


funcs = [Solution().findKthPositive_brute, Solution().findKthPositive_binSearch]

data = [
    ([2, 3, 4, 7, 11], 5, 9),
    ([1, 2, 3, 4], 2, 6),
    ([5, 6, 7], 3, 3),
    ([1, 10, 21, 22, 25], 12, 14),
    ([2], 1, 1),
]

for arg_arr, arg_k, output in data:
    print(f"arr = {arg_arr}, k = {arg_k}\nOutput = {output}")
    for func in funcs:
        print(f"{func.__name__} = {func(arg_arr, arg_k)}")
