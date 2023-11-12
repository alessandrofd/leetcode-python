from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        routes_by_stop = defaultdict(list)
        for route, stops in enumerate(routes):
            for stop in stops:
                routes_by_stop[stop].append(route)

        queue = deque(routes_by_stop[source])
        visited_routes = set()
        visited_stops = set()
        buses = 0

        while queue:
            queue_length = len(queue)
            buses += 1
            for _ in range(queue_length):
                route = queue.popleft()
                for stop in routes[route]:
                    if stop == target:
                        return buses

                    if stop in visited_stops:
                        continue
                    visited_stops.add(stop)

                    for connected_route in routes_by_stop[stop]:
                        if connected_route in visited_routes:
                            continue
                        visited_routes.add(connected_route)

                        queue.append(connected_route)

        return -1


def test_solution():
    """test"""

    funcs = [
        Solution().numBusesToDestination,
    ]

    # fmt: off
    data = [
        [[[1,2,7],[3,6,7]], 1, 6, 2],
        [[[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12, -1],
        [[[1,7],[3,5]], 5, 5, 0]
    ]
    # fmt: on

    for func in funcs:
        for routes, source, target, expected in data:
            assert func(routes, source, target) == expected
