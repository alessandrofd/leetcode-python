from heapq import heapify, heappop
from operator import truediv


class Solution:
    def eliminateMaximum_sort(self, dist, speed):
        n = len(dist)
        arrival_time = [dist[i] / speed[i] for i in range(n)]
        arrival_time.sort()

        for i in range(n):
            if arrival_time[i] <= i:
                return i

        return n

    def eliminateMaximum_heap(self, dist, speed):
        n = len(dist)
        arrival_time = [dist[i] / speed[i] for i in range(n)]
        heapify(arrival_time)

        monsters_killed = 0
        while arrival_time:
            if heappop(arrival_time) <= monsters_killed:
                break
            monsters_killed += 1

        return monsters_killed

    def eliminateMaximum_no_sort(self, dist, speed):
        n = len(dist)
        arrival_time = [-(dist[i] // -speed[i]) for i in range(n)]

        monsters_by_time = [0] * n
        for time in arrival_time:
            if time >= n:
                continue
            monsters_by_time[time] += 1

        for i in range(1, n):
            monsters_by_time[i] += monsters_by_time[i - 1]
            if monsters_by_time[i] > i:
                return i

        return n

    def eliminateMaximum(self, dist, speed):
        n = len(dist)
        arrivals = list(map(truediv, dist, speed))
        arrivals.sort()

        for time, arrival in enumerate(arrivals):
            if arrival <= time:
                return time

        return n


def test_solution():
    """test"""

    funcs = [
        Solution().eliminateMaximum,
    ]

    # fmt: off
    data = [
        [[1, 3, 4], [1, 1, 1], 3],
        [[1, 1, 2, 3], [1, 1, 1, 1], 1],
        [[3, 2, 4], [5, 3, 2], 1],
        [[5, 4, 3, 3, 3], [1, 1, 5, 3, 1], 1, ], 
    ]
    # fmt: on

    for func in funcs:
        for dist, speed, expected in data:
            assert func(dist, speed) == expected
