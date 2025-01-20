class Solution:
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False
        s_index = 0
        t_index = 0
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
        return s_index == len(s)

sol=Solution()
s = "abc"
t = "ahbgdc"
print(sol.isSubsequence(s,t))

'''
Complexity Analysis:
    Time Complexity:
        The loop iterates through the characters in t. 
        In the worst case, all characters in t are checked against s, 
        making the time complexity O(n), where n is the length of t.
        O(n)
    Space Complexity:
        The solution uses a constant amount of space for variables (s_index, t_index), 
        making the space complexity O(1).
'''