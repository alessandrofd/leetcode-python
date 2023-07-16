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
        num_skills = len(req_skills)
        num_people = len(people)

        skill_ids = {skill: i for i, skill in enumerate(req_skills)}
        skills_by_person = [
            reduce(lambda a, b: a | 1 << skill_ids[b], skills, 0) for skills in people
        ]

        dp = [(1 << num_people) - 1] * (1 << num_skills)
        dp[0] = 0

        for skills in range(1, (1 << num_skills)):
            for person in range(num_people):
                other_skills = skills & ~skills_by_person[person]
                if other_skills != skills:
                    team = dp[other_skills] | (1 << person)
                    if team.bit_count() < dp[skills].bit_count():
                        dp[skills] = team

        team_mask = dp[-1]
        team = []
        for person in range(num_people):
            if team_mask & (1 << person):
                team.append(person)
        return team

    def smallestSufficientTeam_top_down_bitmap(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        num_skills = len(req_skills)
        num_people = len(people)

        skill_ids = {skill: i for i, skill in enumerate(req_skills)}
        skills_by_person = [
            reduce(lambda a, b: a | 1 << skill_ids[b], skills, 0) for skills in people
        ]

        dp = [-1] * (1 << num_skills)
        dp[0] = 0

        def dfs(skills):
            if dp[skills] >= 0:
                return dp[skills]

            for person in range(num_people):
                other_skills = skills & ~skills_by_person[person]
                if other_skills != skills:
                    team = dfs(other_skills) | (1 << person)
                    if dp[skills] == -1 or team.bit_count() < dp[skills].bit_count():
                        dp[skills] = team

            return dp[skills]

        team_mask = dfs((1 << num_skills) - 1)
        team = []
        for person in range(num_people):
            if team_mask & (1 << person):
                team.append(person)
        return team

    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        skill_ids = {skill: i for i, skill in enumerate(req_skills)}
        all_skills = [set() for _ in req_skills]
        for person, skills in enumerate(people):
            for skill in skills:
                all_skills[skill_ids[skill]].add(person)

        print(all_skills)

        queue = deque([(all_skills, [])])
        while queue:
            skills, team = queue.popleft()
            rarest_skills = min(skills, key=len)
            for person in rarest_skills:
                remaining_skills = [skill for skill in skills if person not in skill]
                if not remaining_skills:
                    return team + [person]
                queue.append((remaining_skills, team + [person]))


def test_solution():
    """test"""

    funcs = [
        # Solution().smallestSufficientTeam_bottom_up_bitmap,
        # Solution().smallestSufficientTeam_top_down_bitmap,
        Solution().smallestSufficientTeam,
    ]

    # fmt: off
    data = [
        # (['java', 'nodejs', 'reactjs'], [['java'], ['nodejs'], ['nodejs', 'reactjs']], [0,2]),
        # (
        #     ['algorithms', 'math', 'java', 'reactjs', 'csharp', 'aws'],
        #     [
        #         ['algorithms', 'math', 'java'],
        #         ['algorithms', 'math', 'reactjs'],
        #         ['java', 'csharp', 'aws'],
        #         ['reactjs', 'csharp'],
        #         ['csharp', 'math'],
        #         ['aws', 'java'],
        #     ],
        #     [1,2]
        # ),
        (
            [
                "cdkpfwkhlfbps",
                "hnvepiymrmb",
                "cqrdrqty",
                "pxivftxovnpf",
                "uefdllzzmvpaicyl",
                "idsyvyl",
            ],
            [
                [],
                ["hnvepiymrmb"],
                ["uefdllzzmvpaicyl"],
                [],
                ["hnvepiymrmb", "cqrdrqty"],
                ["pxivftxovnpf"],
                ["hnvepiymrmb", "pxivftxovnpf"],
                ["hnvepiymrmb"],
                ["cdkpfwkhlfbps"],
                ["idsyvyl"],
                [],
                ["cdkpfwkhlfbps", "uefdllzzmvpaicyl"],
                ["cdkpfwkhlfbps", "uefdllzzmvpaicyl"],
                ["pxivftxovnpf", "uefdllzzmvpaicyl"],
                [],
                ["cqrdrqty"],
                [],
                ["cqrdrqty", "pxivftxovnpf", "idsyvyl"],
                ["hnvepiymrmb", "idsyvyl"],
                [],
            ],
            [12, 17, 18],
        )
    ]
    # fmt: on
    for skills, people, expected in data:
        for func in funcs:
            assert func(skills, people) == expected
