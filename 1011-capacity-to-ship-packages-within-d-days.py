"""1011. Capacity To Ship Packages Within D Days"""


class Solution:
    """Solution class"""

    def ShipWithinDays(self, weights, days):
        """
        A conveyor belt has packages that must be shipped from one port to another
        within days days.

        The ith package on the conveyor belt has a weight of weights[i]. Each day, we
        load the ship with packages on the conveyor belt (in the order given
        by weights). We may not load more weight than the maximum weight capacity of
        the ship.

        Return the least weight capacity of the ship that will result in all the
        packages on the conveyor belt being shipped within days days.

        Constraints:
            1 <= days <= weights.length <= 5 * 10^4
            1 <= weights[i] <= 500
        """

        total_load = sum(weights)
        max_load = max(weights)

        def feasible(load):
            """Check if load is feasible"""
            current_load = 0
            days_needed = 1
            for weight in weights:
                current_load += weight
                if current_load > load:
                    days_needed += 1
                    current_load = weight
            return days_needed <= days

        lo = max_load
        hi = total_load

        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


solution = Solution()

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
# Output: 15

print(solution.ShipWithinDays(weights, days))

weights = [3, 2, 2, 4, 1, 4]
days = 3
# Output: 6

print(solution.ShipWithinDays(weights, days))


weights = [1, 2, 3, 1, 1]
days = 4
# Output: 3

print(solution.ShipWithinDays(weights, days))


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 10
# Output: 10

print(solution.ShipWithinDays(weights, days))
