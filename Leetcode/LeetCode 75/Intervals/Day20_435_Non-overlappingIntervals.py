class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        k = float('-inf')

        for x, y in intervals:
            if x >= k:
                k = y
            else:
                ans += 1

        return ans

intervals = [[1,2],[2,3],[3,4],[1,3]]
Solution = Solution()
print(Solution.eraseOverlapIntervals(intervals))
'''
Time complexity: 
O(n⋅logn)

We sort intervals, which costs O(n⋅logn). 
Then, we iterate over the input, performing constant time work at each iteration. 
This means the iteration costs O(n), which is dominated by the sort.

Space Complexity: O(logn) or O(n)

The space complexity of the sorting algorithm depends on the implementation of each programming language:
In Python, the sort() function is implemented using the Timsort algorithm, which has a worst-case space complexity of O(n)
'''