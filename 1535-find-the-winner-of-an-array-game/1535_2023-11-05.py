class Solution:
    def getWinner(self, arr, k):
        defending = arr[0]
        wins = 0
        for i in range(1, len(arr)):
            opponent = arr[i]
            if defending > opponent:
                wins += 1
            else:
                defending = opponent
                wins = 1

            if wins == k:
                break

        return defending


def test_solution():
    """test"""

    funcs = [
        Solution().getWinner,
    ]

    # fmt: off
    data = [
        [[2, 1, 3, 5, 4, 6, 7], 2, 5],
        [[3, 2, 1], 10, 3],
    ]
    # fmt: on

    for func in funcs:
        for arr, k, expected in data:
            assert func(arr, k) == expected
