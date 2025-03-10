from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R=deque([])
        D=deque([])
        for i in range(len(senate)):
            if(senate[i]=="R"):
                R.append(i)
            else:
                D.append(i)
        while(R and D):
            if(R[0] < D[0]):
                R.append(len(senate)+R[0])
            else:
                D.append(len(senate)+D[0])
            R.popleft()
            D.popleft()
        return "Radiant" if R else "Dire"

Solution = Solution()
senate = "RDD"
print(Solution.predictPartyVictory(senate))

'''
Time Complexity: O(n), where n is the length of the senate string.
Space Complexity: O(n), where n is the length of the senate string.
'''