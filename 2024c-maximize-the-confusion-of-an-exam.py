"""
A teacher is writing a test with n true/false questions, with 'T' denoting
true and 'F' denoting false. He wants to confuse the students by maximizing
the number of consecutive questions with the same answer (multiple trues or
multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer
to the ith question. In addition, you are given an integer k, the maximum
number of times you may perform the following operation:

    Change the answer key for any question to 'T' or 'F' (i.e., set
    answerKey[i] to 'T' or 'F').

Return the maximum number of consecutive 'T's or 'F's in the answer key after
performing the operation at most k times.

Constraints:
    n == answerKey.length
    1 <= n <= 5 * 10^4
    answerKey[i] is either 'T' or 'F'
    1 <= k <= n
"""

from collections import Counter


class Solution:
    def maxConsecutiveAnswers_bin_search(self, answer_key: str, k: int) -> int:
        return 0

    def maxConsecutiveAnswers_sliding_window(self, answer_key: str, k: int) -> int:
        return 0


def test_solution():
    """test"""

    funcs = [
        Solution().maxConsecutiveAnswers_bin_search,
        Solution().maxConsecutiveAnswers_sliding_window,
    ]

    # fmt: off
    data = [
        # ("TTFF", 2, 4),
        # ("TFFT", 1, 3),
        # ("TTFTTFTT", 1, 5),
        ("FFFTTFTTFT", 3, 8)
    ]
    # fmt: on

    for answer_key, k, expected in data:
        for func in funcs:
            assert func(answer_key, k) == expected
