class Solution:
    def maxProfit(self, prices, fee: int):
        n = len(prices)
        hold, free = -prices[0], 0

        for i in range(1, n):
            tmp = hold
            hold = max(hold, free - prices[i])
            free = max(free, tmp + prices[i] - fee)

        return free
prices = [1,3,2,8,4,9]
fee = 2
Solution = Solution()
print(Solution.maxProfit(prices,fee))
'''
Time complexity: O(n)
We iterate from day 1 to day n - 1, which contains n - 1 steps.
At each step, we update free and hold which takes O(1).
Space complexity: O(1)
We only need to update three parameters tmp, free and hold.
'''