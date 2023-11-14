from collections import defaultdict
from bisect import bisect_left


class Solution:
    def countPalindromicSubsequence_set(self, string):
        first = [-1] * 26
        last = [-1] * 26

        for i, letter in enumerate(string):
            code_point = ord(letter) - 97
            if first[code_point] == -1:
                first[code_point] = i
            last[code_point] = i

        result = 0
        for i in range(26):
            if first[i] == -1 or first[i] == last[i]:
                continue

            between = set()
            for j in range(first[i] + 1, last[i]):
                between.add(string[j])
            result += len(between)

        return result

    def countPalindromicSubsequence(self, string):
        indices_by_letter = defaultdict(list)
        for index, letter in enumerate(string):
            indices_by_letter[letter].append(index)

        ans = 0
        for letter, indices in indices_by_letter.items():
            if len(indices) < 2:
                continue

            if len(indices) > 2:
                ans += 1

            for mid_letter, mid_indices in indices_by_letter.items():
                if letter == mid_letter:
                    continue

                if bisect_left(mid_indices, indices[0]) < bisect_left(
                    mid_indices, indices[-1]
                ):
                    ans += 1
        return ans


def test_solution():
    """test"""

    funcs = [
        Solution().countPalindromicSubsequence,
    ]

    # fmt: off
    data = [
        ['aabca', 3],
        ['adc', 0],
        ['bbcbaba', 4],
    ]
    # fmt: on

    for func in funcs:
        for string, expected in data:
            assert func(string) == expected
