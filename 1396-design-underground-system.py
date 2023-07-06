"""
An underground railway system is keeping track of customer travel times
between different stations. They are using this data to calculate the average
time it takes to travel from one station to another.

Implement the UndergroundSystem class:

    void checkIn(int id, string stationName, int t)

        A customer with a card ID equal to id, checks in at the station
        stationName at time t.

        A customer can only be checked into one place at a time.

    void checkOut(int id, string stationName, int t)

        A customer with a card ID equal to id, checks out from the station
        stationName at time t.

    double getAverageTime(string startStation, string endStation)

        Returns the average time it takes to travel from startStation to
        endStation.

        The average time is computed from all the previous traveling times
        from startStation to endStation that happened directly, meaning a
        check in at startStation followed by a check out from endStation.

        The time it takes to travel from startStation to endStation may be
        different from the time it takes to travel from endStation to
        startStation.

        There will be at least one customer that has traveled from
        startStation to endStation before getAverageTime is called.

You may assume all calls to the checkIn and checkOut methods are consistent.
If a customer checks in at time t1 then checks out at time t2, then t1 < t2.
All events happen in chronological order.

Constraints:
    1 <= id, t <= 10^6
    1 <= stationName.length, startStation.length, endStation.length <= 10
    All strings consist of uppercase and lowercase English letters and digits.
    There will be at most 2 * 10^4 calls in total to checkIn, checkOut, and
    getAverageTime.
    Answers within 10^-5 of the actual value will be accepted.
"""

from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.passengers = {}
        self.trips = defaultdict(lambda: defaultdict(list))

    def checkIn(self, id: int, start_station: str, departure: int) -> None:
        self.passengers[id] = (start_station, departure)

    def checkOut(self, id: int, end_station: str, arrival: int) -> None:
        start_station, departure = self.passengers[id]
        self.trips[start_station][end_station].append(arrival - departure)

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        travel_times = self.trips[start_station][end_station]
        return sum(travel_times) / len(travel_times)


def test1():
    """test"""

    under = UndergroundSystem()
    under.checkIn(45, "Leyton", 3)
    under.checkIn(32, "Paradise", 8)
    under.checkIn(27, "Leyton", 10)
    under.checkOut(45, "Waterloo", 15)
    under.checkOut(27, "Waterloo", 20)
    under.checkOut(32, "Cambridge", 22)

    assert round(under.getAverageTime("Paradise", "Cambridge"), 5) == round(14, 5)
    assert round(under.getAverageTime("Leyton", "Waterloo"), 5) == round(11, 5)

    under.checkIn(10, "Leyton", 24)
    under.getAverageTime("Leyton", "Waterloo")
    under.checkOut(10, "Waterloo", 38)

    assert round(under.getAverageTime("Leyton", "Waterloo"), 5) == round(12.00, 5)


def test2():
    """second test"""
    under = UndergroundSystem()
    under.checkIn(10, "Leyton", 3)
    under.checkOut(10, "Paradise", 8)

    assert round(under.getAverageTime("Leyton", "Paradise"), 5) == round(5, 5)

    under.checkIn(5, "Leyton", 10)
    under.checkOut(5, "Paradise", 16)

    assert round(under.getAverageTime("Leyton", "Paradise"), 5) == round(5.5, 5)

    under.checkIn(2, "Leyton", 21)
    under.checkOut(2, "Paradise", 30)

    assert round(under.getAverageTime("Leyton", "Paradise"), 5) == round(6.66667, 5)
