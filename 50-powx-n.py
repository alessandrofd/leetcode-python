"""
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Constraints:
    -100.0 < x < 100.0
    -2^31 <= n <= 2^31 - 1
    n is an integer.
    Either x is not zero or n > 0.
    -10^4 <= x^n <= 10^4
"""


class Solution:
    def myPow_recursive(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow_recursive(x, -n)

        if n % 2:
            return x * self.myPow_recursive(x * x, (n - 1) // 2)
        return self.myPow_recursive(x * x, n // 2)

    def myPow_iterative(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            if n % 2:
                result *= x
                n -= 1
            else:
                x *= x
                n //= 2

        return result


def test_solution():
    """test"""

    funcs = [
        Solution().myPow_recursive,
        Solution().myPow_iterative,
    ]

    # fmt: off
    data = [
        (2.0, 10, 1024.00000),
        (2.1, 3, 9.26100),
        (2.0, -2, 0.25000),
        (34.00515, -3, 3e-05)
    ]
    # fmt: on
    for x, n, expected in data:
        for func in funcs:
            assert round(func(x, n), 5) == round(expected, 5)
