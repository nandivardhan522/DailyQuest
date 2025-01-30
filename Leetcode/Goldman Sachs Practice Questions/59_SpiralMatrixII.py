from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        Matrix = [[0] * n for _ in range(n)]

        row, col, d = 0, 0, 0
        counter = 1

        for _ in range(n * n):
            Matrix[row][col] = counter
            counter += 1
            nextRow, nextCol = row + directions[d][0], col + directions[d][1]
            if not (0 <= nextRow < n and 0 <= nextCol < n and Matrix[nextRow][nextCol] == 0):
                d = (d + 1) % 4
                nextRow, nextCol = row + directions[d][0], col + directions[d][1]

            row, col = nextRow, nextCol

        return Matrix

n = 5
Solution=Solution()

print(Solution.generateMatrix(n))

'''
Analysis:
Time Complexity:
    The function iterates through the matrix exactly n² times.
    Each operation (assigning values, checking boundaries) is O(1).
    Overall complexity: O(n²).
Space Complexity:
    The matrix Matrix[n][n] requires O(n²) space.
    A few extra variables (integers, tuples) are O(1).
    Overall complexity: O(n²).
'''