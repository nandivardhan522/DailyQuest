class Solution:
    def findCircleNum(self, isConnected) -> int:
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)
        visited=set()
        numberOfProvinces=0
        for start in range(len(isConnected)):
            if start not in visited:
                numberOfProvinces+=1
                dfs(start)
        return numberOfProvinces

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Solution=Solution()
print(Solution.findCircleNum(isConnected))

'''
Time Complexity: O(n^2), where n is the number of cities (nodes).
Space Complexity: O(n), where n is the number of cities (nodes).
'''