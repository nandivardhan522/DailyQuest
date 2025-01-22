from collections import deque
class Solution:
    def orangesRotting(self, grid):
        queue=deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==2):
                    queue.append((i,j))
        dir=[(-1,0),(0,-1),(0,1),(1,0)]
        time=0
        while(queue):
            rotten=False
            for i in range(len(queue)):
                row,col=queue.popleft()
                for r,c in dir:
                    if(0<=row+r<len(grid) and 0<=col+c<len(grid[0])):
                        if(grid[row+r][col+c]==1):
                            queue.append((row+r,col+c))
                            grid[row+r][col+c]=2
                            rotten=True
            time+=int(rotten)
        for i in range(len(grid)):
            if(1 in grid[i]):
                return -1
        return time

sol=Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(sol.orangesRotting(grid))
'''
Time Complexity:
    Traversal:Each cell is visited at most once, so the BFS traversal takes O(m×n), 
        where m is the number of rows and n is the number of columns in the grid.
    Initialization: Scanning the grid to initialize the queue takes O(m×n).
    Overall Time Complexity: O(m×n).

Space Complexity:
    Queue: In the worst case, the queue can hold all the cells in the grid. 
        This requires O(m×n) space.
    Grid: The grid itself is updated in place, so no additional space is used for it.
    Overall Space Complexity: O(m×n).
'''