"""502. IPO"""

from heapq import heappush, heappop


class Solution(object):
    """Solution class"""

    def findMaximizedCapital(self, k, w, profits, capital):
        """
        Suppose LeetCode will start its IPO soon. In order to sell a good price
        of its shares to Venture Capital, LeetCode would like to work on some
        projects to increase its capital before the IPO. Since it has limited
        resources, it can only finish at most k distinct projects before the IPO.
        Help LeetCode design the best way to maximize its total capital after
        finishing at most k distinct projects.

        You are given n projects where the ith project has a pure profit
        profits[i] and a minimum capital of capital[i] is needed to start it.

        Initially, you have w capital. When you finish a project, you will
        obtain its pure profit and the profit will be added to your total
        capital.

        Pick a list of at most k distinct projects from given projects to
        maximize your final capital, and return the final maximized capital.

        The answer is guaranteed to fit in a 32-bit signed integer.

        Constraints:

            1 <= k <= 10^5
            0 <= w <= 10^9
            n == profits.length
            n == capital.length
            1 <= n <= 10^5
            0 <= profits[i] <= 10^4
            0 <= capital[i] <= 10^9
        """

        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()

        # heapq is a min-heap data structure, but we need a max-heap
        # so we will store negated elements
        queue = []
        ptr = 0
        for _ in range(k):
            while ptr < n and projects[ptr][0] <= w:
                # push a negated element to the heap
                heappush(queue, -projects[ptr][1])
                ptr += 1
            if not queue:
                break

            # pop a negated element from the heap
            w += -heappop(queue)

        return w


k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
# Output: 4

print(Solution().findMaximizedCapital(k, w, profits, capital))

k = 3
w = 0
profits = [1, 2, 3]
capital = [0, 1, 2]
# Output: 6

print(Solution().findMaximizedCapital(k, w, profits, capital))
