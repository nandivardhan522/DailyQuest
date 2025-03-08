from collections import defaultdict
class Solution:
    def canVisitAllRooms(self, rooms):
        stack=[]
        d=defaultdict(int)
        stack+=rooms[0]
        while(len(stack)>0):
            if(not d[stack[-1]]):
                d[stack[-1]]=1
                k=stack.pop()
                stack+=rooms[k]
            else:
                stack.pop()
        return not (len(rooms)*(len(rooms)-1)//2 - sum(d.keys()))
rooms = [[1],[2],[3],[]]

Solution = Solution()
print(Solution.canVisitAllRooms(rooms))

'''
Time Complexity: O(N), where N is the total number of keys in all rooms.
Space Complexity: O(N), where N is the total number of keys in all rooms.
'''