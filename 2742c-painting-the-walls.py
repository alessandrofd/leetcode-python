"""
You are given two 0-indexed integer arrays, cost and time, of size n
representing the costs and the time taken to paint n different walls
respectively. There are two painters available:

    A paid painter that paints the ith wall in time[i] units of time and takes
    cost[i] units of money.

    A free painter that paints any wall in 1 unit of time at a cost of 0.
    But the free painter can only be used if the paid painter is already
    occupied.

Return the minimum amount of money required to paint the n walls.

Constraints:
    1 <= cost.length <= 500
    cost.length == time.length
    1 <= cost[i] <= 10^6
    1 <= time[i] <= 500
"""


class Solution:
    def paintWalls_top_down(self, cost: list[int], time: list[int]) -> int:
        """
        Intuitively, we want to put the paid painter on walls that cost less and
        take longer to paint. The longer the paid painter paints, the more we can
        make use of the free painter. It seems extremely difficult to formulate a
        greedy approach since decisions will cascade on top of each other. Which
        walls do we pay for? Which walls do we have the free painter paint?

        Given the constraints n ≤ 500, we should try a dynamic programming
        approach, which will consider all possible decisions.

        Let's say that we spend money and the paid painter paints for t time.
        The paid painter will paint 1 wall, and the free painter will paint
        t walls. Thus, we spend money to paint 1 + t walls.

        This is a variation of the classic knapsack problem. The ith item costs
        cost[i] and paints 1 + time[i] walls. We need to paint n walls while
        minimizing the total cost.

        Let dp(i, remain) be a function that returns the minimum cost to paint
        remain walls when considering index i and beyond. We have two base cases
        here.

        If remain <= 0, we have painted all the walls. We can return 0.

        If i == n, we have run out of walls to put the paid painter on and the
        task is impossible. We return a large value like infinity.

        Now, how do we calculate a given state (i, remain)? For the ith wall, we
        have two options. We can either hire the paid painter for this wall or not
        hire them.

        If we hire them, as mentioned above, we spend cost[i] and paint
        1 + time[i] walls. Then, we move to the next index. Thus, the cost of
        this option is cost[i] + dp(i + 1, remain - 1 - time[i]).

        If we don't hire them, we simply move to the next index. The cost of
        this option is dp(i + 1, remain).

        Let's call the first option paint and the second option dontPaint. Then,
        dp(i, remain) = min(paint, dontPaint).

        This recursive approach is correct, but has an exponential time complexity
        because each dp call creates two more dp calls, some of which may have
        already been calculated. We must memoize our function to avoid repeated
        computation.

        The solution to the original problem will be dp(0, n). We consider all
        walls starting from index 0 and beyond, and we need to paint a total of
        n walls.
        """

        return -1

    def paintWalls_bottom_up(self, cost: list[int], time: list[int]) -> int:
        """
        We can implement the same algorithm iteratively. In top-down, we start at
        the answer (i = 0, remain = n) and work our way down to the base cases:
            remain <= 0
            i == n

        In bottom-up, we will start from these base cases and iterate toward the
        answer. We will use a table dp which is equivalent to the function from the
        previous approach. Here, dp[i][remain] is equal to dp(i, remain) from the
        previous approach.

        We have a for loop for i starting from n - 1 and iterating to 0. Then we
        have a nested for loop for remain starting from 1 and iterating to n. At
        each inner loop iteration, we have a state i, remain. We can calculate this
        state the same way we did in the previous approach - by calculating paint
        and dontPaint.

        Note that when we calculate paint, remain - 1 - time[i] may be less than 0,
        which would cause an index out-of-bound error. We can solve this by using
        max(0, remain - 1 - time[i]) as an index, so any negative value is
        converted to 0. Because the base case is remain <= 0, this will not affect
        the calculations.
        """

        return -1

    def paintWalls_bottom_up_optimized_space(
        self, cost: list[int], time: list[int]
    ) -> int:
        """
        Notice that the recurrence relation to calculate dp[i][remain] only depends
        on dp[i + 1]. For example, when calculating dp[7][remain], we only need the
        value from dp[8] and no longer care about values in dp[9], dp[10], dp[11]
        etc.

        We only need extra space to track the remain dimension. We can replace our
        O(n^2) table with two arrays of length O(n). One array will represent dp[i]
        and the other one will represent dp[i + 1].

        Let's call the table that represents dp[i + 1] prevDp. When we finish
        calculating dp[i], we can set prevDp = dp. Then when we move to the next
        value of i, prevDp will correctly represent dp[i + 1] for the new value
        of i. For example:

            When i = 10, prevDp is analogous to dp[11] from the previous approach,
            and dp is analogous to dp[10]. We calculate dp, then update prevDp = dp.

            When i = 9, prevDp is analogous to dp[10] from the previous approach.
            Notice that we made this happen by updating prevDp in the last step. We
            calculate dp, analogous to dp[9], and update prevDp again when finished.

            When i = 8, prevDp is analogous to dp[9], and so on...

        The first value of i we iterate on is n - 1. Thus, prevDp initially
        represents dp[n], which is one of our base cases - all values should be a
        large value like infinity, except prevDp[0] = 0, which is our other base
        case (remain = 0).
        """

        return -1

    def paintWalls_bottom_up_single_array(
        self, cost: list[int], time: list[int]
    ) -> int:
        return -1


def test_solution():
    """test"""

    funcs = [
        Solution().paintWalls_top_down,
        Solution().paintWalls_bottom_up,
        Solution().paintWalls_bottom_up_optimized_space,
        Solution().paintWalls_bottom_up_single_array,
    ]

    # fmt: off
    data = [
        [[1, 2, 3, 2], [1, 2, 3, 2], 3],
        [[2, 3, 4, 2], [1, 1, 1, 1], 4],
    ]
    # fmt: on
    for func in funcs:
        for cost, time, expected in data:
            assert func(cost, time) == expected
