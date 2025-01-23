class Solution:
    def removeStars(self, s: str) -> str:
        stk=[]
        length=0
        for i in s:
            if length != 0 and i=="*":
                stk.pop()
                length-=1
            elif(length == 0 and i == "*"):
                continue
            else:
                stk.append(i)
                length +=1
        return ''.join(stk)

s = "leet**cod*e"
sol=Solution()
print(sol.removeStars(s))
'''
Efficiency Analysis:
    Time Complexity: 
        You traverse the string s once: O(n), where n=len(s).
        Each operation (append or pop) on the stack is O(1).
        Overall: O(n).
    
    Space Complexity:
        The space used by the stack is proportional to the number of characters in s 
        that are not removed: O(n) in the worst case.
        Overall: O(n).
'''