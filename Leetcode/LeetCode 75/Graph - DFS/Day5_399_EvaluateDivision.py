from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries):
        graph=defaultdict(list)
        variables=set()
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1],values[i]))
            graph[equations[i][1]].append((equations[i][0],1/values[i]))
            variables.add(equations[i][0])
            variables.add(equations[i][1])
        res=[]
        print
        visited=set()
        def dfs(src,dest,prod):
            if(src==dest):
                res.append(prod)
                return True
            visited.add(src)
            for j,k in graph[src]:
                if(j not in visited):
                    if(dfs(j,dest,prod*k)):
                        return True
            return False

        for i in range(len(queries)):
            if(queries[i][0] not in variables or queries[i][1] not in variables):
                res.append(-1)
                continue
            if(not dfs(queries[i][0],queries[i][1],1)):
                res.append(-1)
            visited=set()
        return res

sol=Solution()
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

'''
Complexity Analysis:
    Time Complexity:
        Graph Construction: O(E), where E is the number of equations.
        DFS for Queries: In the worst case, a single DFS traversal explores all nodes (O(V), where 
        V is the number of variables).
        For Q queries, the worst-case time complexity is O(Q⋅V).
    Space Complexity
        Graph storage: O(E).
        Visited set and recursion stack for DFS: O(V).
        Total: O(E+V).
'''

