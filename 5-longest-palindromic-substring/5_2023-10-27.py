class Solution:
    def longestPalindrome_brute_force(self, s: str) -> str:
        n = len(s)

        def check(start, length):
            left = start
            right = start + length - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for length in range(n, 0, -1):
            for start in range(0, n - length + 1):
                if check(start, length):
                    return s[start : start + length]

        return ""

    def longestPalindrome_dp(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        result = [0, 0]

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                result = [i, i + 1]

        for diff in range(2, n):
            for i in range(0, n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    result = [i, j]

        i, j = result
        return s[i : j + 1]

    def longestPalindrome_expand_from_center(self, s: str) -> str:
        n = len(s)

        def check(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            # O comprimento normal seria j-1+1, mas tem que subtrair 2 pois
            # quando sairmos do laço a sustring delimitada por i, j já não é
            # mais um palíndromo
            return j - i - 1

        result = (0, 0)
        max_length = 1

        for i in range(n):
            odd_length = check(i, i)
            if odd_length > max_length:
                diff = odd_length // 2
                result = (i - diff, i + diff)
                max_length = odd_length

            even_length = check(i, i + 1)
            if even_length > max_length:
                diff = even_length // 2 - 1
                result = (i - diff, i + 1 + diff)
                max_length = even_length

        i, j = result
        return s[i : j + 1]


def test_solution():
    """test"""

    funcs = [
        Solution().longestPalindrome_brute_force,
        # Solution().longestPalindrome_dp,
        Solution().longestPalindrome_expand_from_center,
    ]

    # fmt: off
    data = [
        ['babad', 'bab'],
        ['cbbd', 'bb'],
    ]
    # fmt: on

    for func in funcs:
        for s, expected in data:
            assert func(s) == expected
