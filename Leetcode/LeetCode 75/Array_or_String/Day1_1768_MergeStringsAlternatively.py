class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=word1
        b=word2
        res=""
        def rec(a,b,res):
            if(a=="" and b!=""):
                return res+b
            if(a!="" and b==""):
                return res+a
            if(a=="" and b==""):
                return res
            res+=a[0]
            res+=b[0]
            try:
                a=a[1:]
            except:
                a=""
            try:
                b=b[1:]
            except:
                b=""
            return rec(a,b,res)
        return rec(a,b,res)

sol=Solution()
word1 = "abc"
word2 = "pqr"
print(sol.mergeAlternately(word1,word2))
