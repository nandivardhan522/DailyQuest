class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        n = max(candies)
        i = 0
        j = len(candies)
        res = []
        while (i < j):
            if (candies[i] + extraCandies >= n):
                res.append(True)
            else:
                res.append(False)
            i += 1
        return res
sol=Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(sol.kidsWithCandies(candies,extraCandies))

'''
Analysis:
    Complexity Analysis
        Time Complexity:
            Finding Maximum:
                Calculating max(candies) takes O(n), where n is the number of elements in the candies list.
            Iteration:
                The while loop iterates through the list once, contributing O(n).
            Overall Time Complexity:
                O(n)
        Space Complexity:
            The res list stores n boolean values, contributing O(n).
            Overall Space Complexity:
                O(n)
'''