"""
Given a string s, remove duplicate letters so that every letter appears once
and only once. You must make sure your result is the smallest in
lexicographical order among all possible results.

Constraints:
    1 <= s.length <= 10^4
    s consists of lowercase English letters.
"""

from collections import Counter


class Solution:
    def removeDuplicateLetters_map(self, s: str) -> str:
        last_index = {c: i for i, c in enumerate(s)}
        seen = set()
        stack = []
        for i, c in enumerate(s):
            if c in seen:
                continue

            while stack and stack[-1] > c and last_index[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return "".join(stack)

    def removeDuplicateLetters_counter(self, s: str) -> str:
        count = Counter(s)
        seen = set()
        stack = []
        for c in s:
            count[c] -= 1

            if c in seen:
                continue

            while stack and stack[-1] > c and count[stack[-1]]:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return "".join(stack)


def test_solution():
    """test"""

    funcs = [
        # Solution().removeDuplicateLetters_map,
        Solution().removeDuplicateLetters_counter,
    ]

    # fmt: off
    data = [
        # ['bcabc', 'abc'],
        # ['cbacdcbc', 'acdb'],
        # ['leetcode', 'letcod'],
        ['bbcaac', 'bac'],
    ]
    # fmt: on

    for s, expected in data:
        for func in funcs:
            assert func(s) == expected


if __name__ == "__main__":
    print(Solution().removeDuplicateLetters_map("bbcaac"))
