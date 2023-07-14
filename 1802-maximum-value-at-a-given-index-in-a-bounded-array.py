"""
You are given three positive integers: n, index, and maxSum. You want to
construct an array nums (0-indexed) that satisfies the following conditions:

    nums.length == n
    nums[i] is a positive integer where 0 <= i < n.
    abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
    The sum of all the elements of nums does not exceed maxSum.
    nums[index] is maximized.

Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

Constraints:
    1 <= n <= maxSum <= 10^9
    0 <= index < n
"""


class Solution:
    def maxValue(self, n: int, index: int, max_sum: int) -> int:
        def valid(value):
            left = 0
            if value <= index:
                left = (value + 1) * value / 2
                left += index - value + 1
            else:
                left = (value + (value - index)) * (index + 1) / 2

            right = 0
            if value <= n - index:
                right = (value + 1) * value / 2
                right += n - index - value
            else:
                right = (value + (value - (n - 1 - index))) * (n - index) / 2

            return left + right - value <= max_sum

        lo = 1
        hi = max_sum
        while lo <= hi:
            mid = (lo + hi) // 2
            if valid(mid):
                lo = mid + 1
            else:
                hi = mid - 1

        return lo - 1


def test_solution():
    """test"""

    funcs = [
        Solution().maxValue,
    ]

    # fmt: off
    data = [
        (4, 2, 6, 2),
        (6, 1, 10, 3),
        (8, 7, 14, 4),
        (1, 0, 24, 24),
        (4, 0, 4, 1),
    ]
    # fmt: on
    for n, index, max_sum, expected in data:
        for func in funcs:
            assert func(n, index, max_sum) == expected
