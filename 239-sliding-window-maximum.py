"""
 * You are given an array of integers nums, there is a sliding window of size k
 * which is moving from the very left of the array to the very right. You can
 * only see the k numbers in the window. Each time the sliding window moves
 * right by one position.
 *
 * Return the max sliding window.
 *
 * Constraints:
 *    1 <= nums.length <= 10^5
 *    -10^4 <= nums[i] <= 10^4
 *    1 <= k <= nums.length
"""
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Approach: Monotonic Deque
        """
        if k == 1:
            return nums

        n = len(nums)

        if k == n:
            return [max(nums)]

        queue = deque()

        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

        result = [nums[queue[0]]]

        for i in range(k, n):
            if queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            result.append(nums[queue[0]])

        return result


def test_solution():
    """test"""

    funcs = [
        Solution().maxSlidingWindow,
    ]

    # fmt: off
    data = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
    ]
    # fmt: on
    for nums, k, expected in data:
        for func in funcs:
            assert func(nums, k) == expected


if __name__ == "__main__":
    pass
