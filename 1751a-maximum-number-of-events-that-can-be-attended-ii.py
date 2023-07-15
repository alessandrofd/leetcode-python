"""
You are given an array of events where events[i] = [startDayi, endDayi, valuei].
The ith event starts at startDayi and ends at endDayi, and if you attend this
event, you will receive a value of valuei. You are also given an integer k
which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event,
you must attend the entire event. Note that the end day is inclusive: that is,
you cannot attend two events where one of them starts and the other ends on
the same day.

Return the maximum sum of values that you can receive by attending events.

Constraints:
    1 <= k <= events.length
    1 <= k * events.length <= 10^6
    1 <= startDayi <= endDayi <= 10^9
    1 <= valuei <= 10^6
"""


# Programação dinâminca
# Dimensões: eventos avaliados e quantidade de eventos que ainda podem ser
# frequentados: dp[i, count], onde 0 <= i < n e 0<= count <= k
# Condição inicial: No top-down dp[i, count] = 0 se i == n ou count == 0
# Transição: max(dp[i+1, count], events[i][2] + dp[next_event, count-1]), onde
# next_event é o próximo evento em que o início é posterior ao término
# do evento i
# Resultado final: dp[0, k]


from typing import List
from bisect import bisect_right


class Solution:
    def maxValue_top_down_bin_search(self, events: List[List[int]], k: int) -> int:
        return 0

    def maxValue_bottom_up_bin_search(self, events: List[List[int]], k: int) -> int:
        return 0

    def maxValue_top_down_cached_bin_search(
        self, events: List[List[int]], k: int
    ) -> int:
        return 0

    def maxValue_top_down_no_bin_search(self, events: List[List[int]], k: int) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().maxValue_top_down_bin_search,
        Solution().maxValue_bottom_up_bin_search,
        Solution().maxValue_top_down_cached_bin_search,
        Solution().maxValue_top_down_no_bin_search,
    ]

    # fmt: off
    data = [
        ([[1,2,4],[3,4,3],[2,3,1]], 2, 7),
        ([[1,2,4],[3,4,3],[2,3,10]], 2, 10),
        ([[1,1,1],[2,2,2],[3,3,3],[4,4,4]], 3, 9),
        ([[1,1,1],[2,2,2],[3,3,3],[4,4,4]], 3, 9),
        ([[21,77,43],[2,74,47],[6,59,22],[47,47,38],[13,74,57],[27,55,27],[8,15,8]], 4, 57),
    ]
    # fmt: on
    for events, k, expected in data:
        for func in funcs:
            assert func(events, k) == expected
