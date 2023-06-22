"""
Given two integer arrays pushed and popped each with distinct values,
return true if this could have been the result of a sequence of push and pop
operations on an initially empty stack, or false otherwise.

Constraints:
    1 <= pushed.length <= 1000
    0 <= pushed[i] <= 1000
    All the elements of pushed are unique.
    popped.length == pushed.length
    popped is a permutation of pushed.
"""


class Solution:
    def validateStackSequences(self, pushed, popped):
        pass


def test_solution():
    """test"""

    funcs = [
        Solution().validateStackSequences,
    ]

    data = [
        ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
    ]

    for pushed, popped, output in data:
        for func in funcs:
            assert func(pushed, popped) == output
