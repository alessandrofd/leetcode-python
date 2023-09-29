"""
 * You are given a list of airline tickets where tickets[i] = [fromi, toi]
 * represent the departure and the arrival airports of one flight. Reconstruct
 * the itinerary in order and return it.
 *
 * All of the tickets belong to a man who departs from "JFK", thus, the
 * itinerary must begin with "JFK". If there are multiple valid itineraries, you
 * should return the itinerary that has the smallest lexical order when read as
 * a single string.
 *
 *    For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than
 *    ["JFK", "LGB"].
 *
 * You may assume all tickets form at least one valid itinerary. You must use
 * all the tickets once and only once.
 *
 * Constraints:
 *    1 <= tickets.length <= 300
 *    tickets[i].length == 2
 *    fromi.length == 3
 *    toi.length == 3
 *    fromi and toi consist of uppercase English letters.
 *    fromi != toi
"""

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        flights = defaultdict(list)
        for departure, destination in tickets:
            flights[departure].append(destination)

        for destinations in flights.values():
            destinations.sort(reverse=True)

        itinerary = []

        def visit(airport: str) -> None:
            while flights[airport]:
                visit(flights[airport].pop())

            itinerary.append(airport)

        visit("JFK")
        return itinerary[::-1]


def test_solution():
    """test"""

    # fmt: off
    funcs = [
        Solution().findItinerary,
    ]

    data = [
        [
            [
                ['MUC', 'LHR'],
                ['JFK', 'MUC'],
                ['SFO', 'SJC'],
                ['LHR', 'SFO'],
            ],
            ['JFK', 'MUC', 'LHR', 'SFO', 'SJC'],
        ],
        [
            [
                ['JFK', 'SFO'],
                ['JFK', 'ATL'],
                ['SFO', 'ATL'],
                ['ATL', 'JFK'],
                ['ATL', 'SFO'],
            ],
            ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'],
        ],
        [
            [
                ['JFK', 'KUL'],
                ['JFK', 'NRT'],
                ['NRT', 'JFK'],
            ],
            ['JFK', 'NRT', 'JFK', 'KUL'],
        ],
        [
            [
                ['EZE', 'TIA'],
                ['EZE', 'HBA'],
                ['AXA', 'TIA'],
                ['JFK', 'AXA'],
                ['ANU', 'JFK'],
                ['ADL', 'ANU'],
                ['TIA', 'AUA'],
                ['ANU', 'AUA'],
                ['ADL', 'EZE'],
                ['ADL', 'EZE'],
                ['EZE', 'ADL'],
                ['AXA', 'EZE'],
                ['AUA', 'AXA'],
                ['JFK', 'AXA'],
                ['AXA', 'AUA'],
                ['AUA', 'ADL'],
                ['ANU', 'EZE'],
                ['TIA', 'ADL'],
                ['EZE', 'ANU'],
                ['AUA', 'ANU'],
            ],
            [ 'JFK', 'AXA', 'AUA', 'ADL', 'ANU', 'AUA', 'ANU', 'EZE', 'ADL', 'EZE', 'ANU', 'JFK', 'AXA', 'EZE', 'TIA', 'AUA', 'AXA', 'TIA', 'ADL', 'EZE', 'HBA', ],
        ],
    ]
    # fmt: on

    for tickets, expected in data:
        for func in funcs:
            assert func(tickets) == expected


if __name__ == "__main__":
    pass
