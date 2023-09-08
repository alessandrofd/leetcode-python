"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly
above it.

Constraints:
    1 <= numRows <= 30
"""


class Solution:
    def generate(self, num_rows):
        pass


def test_solution():
    """test"""

    # fmt: off
    funcs = [
        Solution().generate,
    ]

    data = [
        [5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]],
        [1, [[1]]],
    ]
    # fmt: on

    for num_rows, expected in data:
        for func in funcs:
            assert func(num_rows) == expected


if __name__ == "__main__":
    # nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # ll = array_to_linked_list(nodes)
    # print(linked_list_to_array(ll))
    pass
