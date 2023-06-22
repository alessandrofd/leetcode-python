"""
You are given an array time where time[i] denotes the time taken by the ith
bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can
start immediately after completing the current trip. Also, each bus operates
independently; that is, the trips of one bus do not influence the trips of
any other bus.

You are also given an integer totalTrips, which denotes the number of trips
all buses should make in total. Return the minimum time required for all
buses to complete at least totalTrips trips

Constraints:
    1 <= time.length <= 10^5
    1 <= time[i], totalTrips <= 10^7
"""

from typing import List


class Solution:  # pylint: disable=too-few-public-methods
    """Solution class"""

    def minimumTime(  # pylint: disable=invalid-name
        self, times: List[int], total_trips: int
    ) -> int:
        """Binary Search"""

        def enough_time(given_time):
            trips = 0
            for time in times:
                trips += given_time // time
                if trips >= total_trips:
                    return True
            return False

        lo = 1
        hi = max(times) * total_trips
        while lo < hi:
            mid = (lo + hi) // 2
            if enough_time(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo


funcs = [Solution().minimumTime]

data = [
    ([1, 2, 3], 5, 3),
    ([2], 1, 2),
    ([2, 3, 9], 7, 9),
]

for arg_times, arg_total_trips, output in data:
    print(f"arr = {arg_times}, k = {arg_total_trips}\nOutput = {output}")
    for func in funcs:
        print(f"{func.__name__} = {func(arg_times, arg_total_trips)}")
