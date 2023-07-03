"""
We have n buildings numbered from 0 to n - 1. Each building has a number of
employees. It's transfer season, and some employees want to change
the building they reside in.

You are given an array requests where requests[i] = [fromi, toi] represents
an employee's request to transfer from building fromi to building toi.

All buildings are full, so a list of requests is achievable only if for each
building, the net change in employee transfers is zero. This means the number
of employees leaving is equal to the number of employees moving in. For
example if n = 3 and two employees are leaving building 0, one is leaving
building 1, and one is leaving building 2, there should be two employees
moving to building 0, one employee moving to building 1, and one employee
moving to building 2.

Return the maximum number of achievable requests.

Constraints:
    1 <= n <= 20
    1 <= requests.length <= 16
    requests[i].length == 2
    0 <= fromi, toi < n
"""

from typing import List


class Solution:
    def maximumRequests(self, num_buildings: int, requests: List[List[int]]) -> int:
        num_requests = len(requests)
        balance = [0] * num_buildings
        max_requests = 0

        def backtrack(curr_request, accepted_requests):
            nonlocal max_requests

            if curr_request == num_requests:
                if all(b == 0 for b in balance):
                    max_requests = max(max_requests, accepted_requests)
                return

            # deny request
            backtrack(curr_request + 1, accepted_requests)

            # accept request
            from_building, to_building = requests[curr_request]

            balance[from_building] -= 1
            balance[to_building] += 1

            backtrack(curr_request + 1, accepted_requests + 1)

            balance[from_building] += 1
            balance[to_building] -= 1

        backtrack(0, 0)
        return max_requests


def test_solution():
    """test"""

    funcs = [
        Solution().maximumRequests,
    ]

    # fmt: off
    data = [
        (5, [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]], 5),
        (3, [[0,0],[1,2],[2,1]], 3),
        (4, [[0,3],[3,1],[1,2],[2,0]], 4),
    ]
    # fmt: on
    for cookies, k, expected in data:
        for func in funcs:
            assert func(cookies, k) == expected
