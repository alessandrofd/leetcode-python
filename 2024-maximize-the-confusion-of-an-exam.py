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
        n = len(answer_key)

        def is_valid_window(window):
            trues = Counter(answer_key[:window])["T"]

            if trues <= k or trues >= window - k:
                return True

            for i in range(window, n):
                if answer_key[i - window] == "T":
                    trues -= 1
                if answer_key[i] == "T":
                    trues += 1
                if trues <= k or trues >= window - k:
                    return True

            return False

        lo = 1
        hi = n + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if is_valid_window(mid):
                lo = mid + 1
            else:
                hi = mid

        return lo - 1

    def maxConsecutiveAnswers_sliding_window(self, answer_key: str, k: int) -> int:
        n = len(answer_key)
        max_window = 0
        left = 0
        trues = 0

        for right in range(n):
            window = right - left + 1
            if answer_key[right] == "T":
                trues += 1

            if trues <= k or trues >= window - k:
                max_window += 1
            else:
                if answer_key[left] == "T":
                    trues -= 1
                left += 1

        return max_window


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
