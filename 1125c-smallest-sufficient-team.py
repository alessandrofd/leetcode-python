"""
In a project, you have a list of required skills req_skills, and a list
of people. The ith person people[i] contains a list of skills that
the person has.

Consider a sufficient team: a set of people such that for every required
skill in req_skills, there is at least one person in the team who has that
skill. We can represent these teams by the index of each person.

    For example, team = [0, 1, 3] represents the people with skills people[0],
    people[1], and people[3].

Return any sufficient team of the smallest possible size, represented by
the index of each person. You may return the answer in any order.

It is guaranteed an answer exists.

Constraints:
    1 <= req_skills.length <= 16
    1 <= req_skills[i].length <= 16
    req_skills[i] consists of lowercase English letters.
    All the strings of req_skills are unique.
    1 <= people.length <= 60
    0 <= people[i].length <= 16
    1 <= people[i][j].length <= 16
    people[i][j] consists of lowercase English letters.
    All the strings of people[i] are unique.
    Every skill in people[i] is a skill in req_skills.
    It is guaranteed a sufficient team exists.
"""

from typing import List
from functools import reduce
from collections import deque


class Solution:
    def smallestSufficientTeam_bottom_up_bitmap(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        return [0]

    def smallestSufficientTeam_top_down_bitmap(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        return [0]

    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        return [0]


def test_solution():
    """test"""

    funcs = [
        Solution().smallestSufficientTeam_bottom_up_bitmap,
        Solution().smallestSufficientTeam_top_down_bitmap,
        Solution().smallestSufficientTeam,
    ]

    # fmt: off
    data = [
        (['java', 'nodejs', 'reactjs'], [['java'], ['nodejs'], ['nodejs', 'reactjs']], [0,2]),
        (
            ['algorithms', 'math', 'java', 'reactjs', 'csharp', 'aws'],
            [
                ['algorithms', 'math', 'java'],
                ['algorithms', 'math', 'reactjs'],
                ['java', 'csharp', 'aws'],
                ['reactjs', 'csharp'],
                ['csharp', 'math'],
                ['aws', 'java'],
            ],
            [1,2]
        ),
    ]
    # fmt: on
    for skills, people, expected in data:
        for func in funcs:
            assert func(skills, people) == expected
