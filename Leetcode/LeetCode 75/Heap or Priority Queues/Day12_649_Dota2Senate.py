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

senate = "RD"
sol=Solution()
print(sol.predictPartyVictory(senate))

"""
Time Complexity:
    Initialization: Populating R and D takes O(n).
    Processing: Each senator is processed at most once per round, leading to O(n) rounds in the worst case.
    Queue Operations: All popleft() and append() operations are O(1).
    Overall Complexity: O(n).
Space Complexity:
    Two deques (R and D) each store at most O(n) elements.
    No additional significant space is used.
    Overall Complexity: O(n).
"""