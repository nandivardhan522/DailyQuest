class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        dp=[0]*len(cost)
        for i in range(2,len(cost)):
            dp[i] += min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])

        return min(dp[-1]+cost[-1],dp[-2]+cost[-2])


cost = [10,15,20]
Solution = Solution()
print(Solution.minCostClimbingStairs(cost))

'''
Time and Space Complexity
Time Complexity: O(n) → We iterate through the cost list once.
Space Complexity: O(n) → We use an extra dp array of size n.
'''
