from collections import Counter
class Solution:
    def equalPairs(self, grid):
        n = len(grid)
        row_count = Counter(tuple(row) for row in grid)
        count = 0
        for col in range(n):
            column = tuple(grid[row][col] for row in range(n))
            count += row_count[column]

        return count

grid = [[3,2,1],[1,7,6],[2,7,7]]
sol=Solution()
print(sol.equalPairs(grid))
'''
Complexity Analysis
    Time Complexity:
        Constructing the row_count: O(n^2), where n is the size of the grid.
        Extracting columns and counting matches: O(n^2).
        Overall: O(n^2).
    Space Complexity:
        Storing row tuples in Counter: O(n^2).
'''