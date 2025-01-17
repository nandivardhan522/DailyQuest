class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        gcd_len = gcd(len(str1), len(str2))
        candidate = str1[:gcd_len]
        if candidate * (len(str1) // gcd_len) == str1 and candidate * (len(str2) // gcd_len) == str2:
            return candidate
        return ""
sol=Solution()
str1 = "ABCABC"
str2 = "ABC"
print(sol.gcdOfStrings(str1,str2))

'''
Complexity Analysis:
    Time Complexity:
        GCD Calculation:
            The Euclidean algorithm runs in O(log(min(a,b))), where a and b are the lengths of str1 and str2.
        Validation:
            Constructing the repeated string takes O(n+m), where n=len(str1) and m=len(str2).
        Overall Time Complexity:
            O(log(min(a,b))+n+m)
    Space Complexity:
        The recursive gcd function has a stack space complexity of O(log(min(a,b))).
        No additional data structures are used apart from the candidate string.
        Overall Space Complexity:
            O(log(min(a,b)))
'''