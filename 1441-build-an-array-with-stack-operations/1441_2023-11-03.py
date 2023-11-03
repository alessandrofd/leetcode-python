class Solution:
    def buildArray(self, target, n):
        result = []
        i = 1

        for num in target:
            while i < num:
                result.append("Push")
                result.append("Pop")
                i += 1

            result.append("Push")
            i += 1

        return result


def test_solution():
    """test"""

    funcs = [
        Solution().buildArray,
    ]

    # fmt: off
    data = [
        [[1, 3], 3, ['Push', 'Push', 'Pop', 'Push']],
        [[1, 2, 3], 3, ['Push', 'Push', 'Push']],
        [[1, 2], 4, ['Push', 'Push']],
    ]
    # fmt: on

    for func in funcs:
        for target, n, expected in data:
            assert func(target, n) == expected
