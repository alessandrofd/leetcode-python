from itertools import accumulate


class Solution:
    def garbageCollection(self, garbage, travel):
        prefix_sum = [0, *accumulate(travel)]

        last_stop = dict((("M", False), ("P", False), ("G", False)))
        all_stops = False

        result = 0

        for i in range(len(garbage) - 1, -1, -1):
            result += len(garbage[i])

            if all_stops:
                continue

            for material in garbage[i]:
                if not last_stop[material]:
                    result += prefix_sum[i]
                    last_stop[material] = True
                    all_stops = all(last_stop.values())

        return result


def test_solution():
    """test"""

    # fmt: off
    funcs = [
        Solution().garbageCollection
    ]

    data = [
        [['G', 'P', 'GP', 'GG'], [2, 4, 3], 21],
        [['MMM', 'PGM', 'GP'], [3, 10], 37],
    ]
    # fmt: on

    for func in funcs:
        for garbage, travel, expected in data:
            assert func(garbage, travel) == expected
