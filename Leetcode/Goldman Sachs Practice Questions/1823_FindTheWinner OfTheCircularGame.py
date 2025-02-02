class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[]
        for i in range(1,n+1):
            l.append(i)
        i=0
        k-=1
        while(len(l)!=1):
            next_ = (i+k)%len(l)
            l.pop(next_)
            i=next_%len(l)
        return l[0]

n = 5
k = 2
Solution = Solution()
print(Solution.findTheWinner(n,k))

'''
Analysis:
Time complexity : 
The loop runs (n-1) times, as we remove one element in each iteration.
l.pop(next_) in a list is O(n) in worst case (since elements must be shifted after removal).
O(n^2)
Space complexity: 
l stores n elements initially → O(n)
'''