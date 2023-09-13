"""
There are n children standing in a line. Each child is assigned a rating
value given in the integer array ratings.

You are giving candies to these children subjected to the following
requirements:

    Each child must have at least one candy.

    Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the
candies to the children.

Constraints:
    n == ratings.length
    1 <= n <= 2 * 10^4
    0 <= ratings[i] <= 2 * 10^4
"""


from typing import List


class Solution:
    def candy_brute_force(self, ratings: List[int]) -> int:
        """Brute force - TLE"""
        n = len(ratings)
        if n <= 1:
            return n

        candies = [1] * n

        changed = True
        while changed:
            changed = False
            for i in range(n):
                if (
                    i > 0
                    and ratings[i] > ratings[i - 1]
                    and candies[i] <= candies[i - 1]
                ):
                    candies[i] = candies[i - 1] + 1
                    changed = True

                if (
                    i < n - 1
                    and ratings[i] > ratings[i + 1]
                    and candies[i] <= candies[i + 1]
                ):
                    candies[i] = candies[i + 1] + 1
                    changed = True

        return sum(candies)

    def candy_two_arrays(self, ratings: List[int]) -> int:
        """Two arrays"""
        n = len(ratings)
        if n <= 1:
            return n

        left_to_right = [1] * n
        right_to_left = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left_to_right[i] = left_to_right[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_to_left[i] = right_to_left[i + 1] + 1

        return sum(
            max(left, right) for left, right in zip(left_to_right, right_to_left)
        )

    def candy_single_array(self, ratings: List[int]) -> int:
        """Single array"""
        n = len(ratings)
        if n <= 1:
            return n

        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

    def candy_single_pass(self, ratings: List[int]) -> int:
        """Single pass"""
        n = len(ratings)
        if n <= 1:
            return n

        candies = 1
        up, down, peak = 0, 0, 0
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                up, down = up + 1, 0
                peak = up
                candies += up + 1
            elif ratings[i] < ratings[i - 1]:
                up, down = 0, down + 1
                candies += down + 1
                if peak >= down:
                    candies -= 1

            else:
                up, down, peak = 0, 0, 0
                candies += 1

            # print(f"previous = {ratings[i-1]}, current = {ratings[i]}")
            # print(f"up = {up}, down = {down}, peak = {peak}")

        return candies


def test_solution():
    """test"""

    # fmt: off
    funcs = [
        Solution().candy_brute_force,
        Solution().candy_two_arrays,
        Solution().candy_single_array,
        Solution().candy_single_pass,
    ]

    data = [
        [[1, 0, 2], 5],
        [[1, 2, 2], 4],
        [[1, 3, 2, 2, 1], 7]
    ]
    # fmt: on

    for ratings, expected in data:
        for func in funcs:
            assert func(ratings) == expected


if __name__ == "__main__":
    pass
