class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

sol=Solution()
s = "the sky is blue"
print(sol.reverseWords(s))

'''
Time Complexity:
    Splitting the String:O(n), where n is the length of the string s.
    Reversing the List: O(w), where w is the number of words.
    Joining the Words: O(n).
    Overall:
        O(n)
Space Complexity:
    O(w), where w is the number of words.
    Output String: O(n), as the result string will have a length proportional to n.
    Overall: O(n)
'''