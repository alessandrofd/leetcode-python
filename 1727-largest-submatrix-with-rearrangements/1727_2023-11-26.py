class Solution:
    def largestSubmatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        max_area = 0
        prev_heights = []
        for row in range(m):
            heights = []
            seen = [False] * n

            for height, col in prev_heights:
                if matrix[row][col] == 1:
                    heights.append((height + 1, col))
                    seen[col] = True

            for col in range(n):
                if matrix[row][col] == 1 and not seen[col]:
                    heights.append((1, col))

            for i, (height, _) in enumerate(heights):
                max_area = max(max_area, height * (i + 1))

            prev_heights = heights

        return max_area

    def largestSubmatrix_sort(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        result = sum(matrix[0])
        for row in range(1, m):
            for col in range(n):
                if matrix[row][col] == 1:
                    matrix[row][col] += matrix[row - 1][col]

            sorted_row = sorted(matrix[row], reverse=True)
            for col in range(n):
                result = max(result, sorted_row[col] * (col + 1))

        return result


def test_solution():
    """test solution"""

    funcs = [
        Solution().largestSubmatrix,
        Solution().largestSubmatrix_sort,
    ]

    data = [
        [[[0, 0, 1], [1, 1, 1], [1, 0, 1]], 4],
        [[[1, 0, 1, 0, 1]], 3],
        [[[1, 1, 0], [1, 0, 1]], 2],
    ]

    for f in funcs:
        for matrix, expected in data:
            assert f(matrix) == expected
