class Solution:
    def maxVowels(self, s, k):
        v_c=0
        vowels=["a","e","i","o","u"]
        for i in range(0,k):
            if(s[i] in vowels):
                v_c+=1
        res=0
        res=max(v_c,res)
        i=1
        j=k
        while(j<len(s)):
            if(s[i-1]in vowels):
                v_c-=1
            if(s[j] in vowels):
                v_c+=1
            res=max(v_c,res)
            j+=1
            i+=1
        return res
s = "abciiidef"
k = 3
sol=Solution()
print(sol.maxVowels(s,k))
'''
Complexity Analysis:
    Time Complexity:
        Initial Vowel Count:Calculating the number of vowels in the first k-length substring takes O(k).
        Sliding Window: Iterating through the rest of the string (n−k iterations) involves constant work per iteration. 
        This takes O(n−k).
        Total:
            O(k)+O(n−k)=O(n)
    Space Complexity:
        The algorithm uses constant space for variables like v_c, res, and vowels. 
        Space complexity: O(1)
'''