class Solution:
    def merge(self, intervals):
        res=[]
        intervals.sort(key=lambda x:x[0])
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if(intervals[i][0]<=res[-1][1]):
                if(intervals[i][1]>=res[-1][1]):
                    res[-1][1]=intervals[i][1]
            else:
                res.append(intervals[i])
        return res

sol=Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(sol.merge(intervals))

'''
Complexity Analysis
    Time Complexity:
        Sorting: Sorting the intervals takes O(nlogn), where n is the number of intervals.
        Iteration: Iterating through the intervals takes O(n).
        Overall: 
            O(nlogn)
    Space Complexity:
        The res list is used to store the merged intervals, requiring O(n) space in the worst case.
        Overall:
            O(n)
'''