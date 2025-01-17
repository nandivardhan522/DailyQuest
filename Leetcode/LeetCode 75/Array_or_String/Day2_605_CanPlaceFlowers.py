class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        res=0
        i=0
        j = len(flowerbed) - 1
        if(n==0):
            return True
        if(j==0 and n==1):
            return not(flowerbed[0])
        if(flowerbed[i]==0 and flowerbed[i+1]==0):
            res+=1
            flowerbed[i] = 1
        i+=1
        while(i<j):
            if(sum(flowerbed[i-1:i+2])==0):
                flowerbed[i]=1
                res+=1
            i+=1
        if(flowerbed[j]==0 and flowerbed[j-1]==0):
            res+=1
            flowerbed[j]=1
        return res>=n

sol=Solution()
flowerbed = [1,0,0,0,1]
n = 1
print(sol.canPlaceFlowers(flowerbed,n))
'''
Complexity Analysis
    Time Complexity:
        The loop iterates through the flowerbed once.
        Each operation inside the loop (checking conditions and updating values) is O(1).
        O(n)
    Space Complexity:
    The algorithm modifies the input list flowerbed in place and uses constant extra space for variables.
    O(1)
'''