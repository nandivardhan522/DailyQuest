class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        res=""
        while(i<len(word1) and j <len(word2)):
            res += word1[i]+word2[j]
            i+=1
            j+=1
        if(i<len(word1)):
            res+=word1[i:]
        elif j<len(word2):
            res+=word2[j:]
        return res

word1 = "abc"
word2 = "pqr"
Solution = Solution()
print(Solution.mergeAlternately(word1,word2))