from collections import defaultdict


class Solution:
    def sortVowels(self, s):
        letters = list(s)
        sorted_vowels = "AEIOUaeiou"
        vowel_pos = []

        freqs = defaultdict(int)
        for pos, letter in enumerate(letters):
            if letter in sorted_vowels:
                vowel_pos.append(pos)
                freqs[letter] += 1

        curr_vowel = 0
        curr_freq = freqs[sorted_vowels[curr_vowel]]

        for pos in vowel_pos:
            while curr_freq == 0:
                curr_vowel += 1
                curr_freq = freqs[sorted_vowels[curr_vowel]]

            letters[pos] = sorted_vowels[curr_vowel]

            curr_freq -= 1

        return "".join(letters)


def test_solution():
    """test"""

    funcs = [
        Solution().sortVowels,
    ]

    # fmt: off
    data = [
        ['lEetcOde', 'lEOtcede'],
        ['lYmpH', 'lYmpH'],
    ]
    # fmt: on

    for func in funcs:
        for s, expected in data:
            assert func(s) == expected
