"""
Two strings X and Y are similar if we can swap two letters (in different
positions) of X, so that it equals Y. Also two strings X and Y are similar if
they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2),
and "rats" and "arts" are similar, but "star" is not similar to "tars",
"rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats",
"arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group
even though they are not similar.  Formally, each group is such that a word
is in the group if and only if it is similar to at least one other word in
the group.

We are given a list strs of strings where every string in strs is an anagram
of every other string in strs. How many groups are there?

Constraints:
    1 <= strs.length <= 300
    1 <= strs[i].length <= 300
    strs[i] consists of lowercase letters only.
    All words in strs have the same length and are anagrams of each other.
 """

# Aplicação de DSU. A cada union(i, j) efetiva subtrai-se um do número de
# componentes finais. Se todas as strings fizerem parte dos mesmo grupo
# componentes == 1


from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        num_strs = len(strs)
        parents = list(range(num_strs))
        ranks = [1] * num_strs
        components = num_strs

        def find(i: int) -> int:
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]

        def union(i: int, j: int) -> int:
            nonlocal components

            i = find(i)
            j = find(j)

            if i == j:
                return 0

            if ranks[i] < ranks[j]:
                parents[j] = i
                ranks[i] += ranks[j]
            else:
                parents[i] = j
                ranks[j] += ranks[i]

            components -= 1
            return 1

        for i in range(num_strs - 1):
            for j in range(1, num_strs):
                diffs = 0
                for k in range(len(strs[0])):
                    if strs[i][k] != strs[j][k]:
                        diffs += 1
                    if diffs > 2:
                        break
                if diffs <= 2:
                    union(i, j)

        return components


def test_solution():
    """test"""

    funcs = [
        Solution().numSimilarGroups,
    ]

    data = [
        (["tars", "rats", "arts", "star"], 2),
        (["omv", "ovm"], 1),
    ]

    for strs, expected in data:
        for func in funcs:
            assert func(strs) == expected
