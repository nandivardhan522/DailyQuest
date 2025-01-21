from collections import deque
class Solution:
    def nearestExit(self, maze, entrance) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set()
        visited.add((entrance[0], entrance[1]))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                    if (nr, nc) not in visited:
                        if (nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1) and [nr, nc] != entrance:
                            return dist + 1
                        visited.add((nr, nc))
                        queue.append((nr, nc, dist + 1))

        return -1

maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]
sol=Solution()
print(sol.nearestExit(maze,entrance))

'''
Complexity Analysis:
    Time Complexity:
        Graph Traversal: Each cell is visited at most once. 
            Total cells: O(m⋅n), where m is the number of rows and n is the number of columns.
        Queue Operations:
            Adding and removing from the deque is O(1).
        Overall: O(m⋅n).
        
    Space Complexity:
        Visited Set:
            Stores up to m⋅n cells: O(m⋅n).
        Queue:
            At most O(m⋅n) elements: O(m⋅n).
        Overall: O(m⋅n).
'''