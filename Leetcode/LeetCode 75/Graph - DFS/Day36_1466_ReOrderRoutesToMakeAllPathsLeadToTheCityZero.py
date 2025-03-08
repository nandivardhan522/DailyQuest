from collections import defaultdict,deque
class Solution():
    def minReorder(self, n: int, connections) -> int:
        graph=defaultdict(dict)
        ans=0
        for i,j in connections:
            graph[i][j]=1
            graph[j][i]=0
        visited=set()
        visited.add(0)
        queue=deque([0])
        while(queue):
            currnode=queue.popleft()
            for neighbor, score in graph[currnode].items():
                if neighbor not in visited:
                    ans+=score
                    queue.append(neighbor)
                    visited.add(neighbor)
        return ans
Solution = Solution()
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(Solution.minReorder(n,connections))
'''
Time Complexity: O(E), where E is the number of connections.
Space Complexity: O(E), where E is the number of connections.
'''