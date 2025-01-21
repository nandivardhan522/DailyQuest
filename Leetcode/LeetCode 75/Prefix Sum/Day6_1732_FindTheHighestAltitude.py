class Solution:
    def largestAltitude(self, gain):
        res = [0]
        maxi = 0
        for i in gain:
            a = res[-1] + i
            maxi = max(maxi, a)
            res.append(a)
        return maxi

sol=Solution()
gain = [-5,1,5,0,-7]
print(sol.largestAltitude(gain))
'''
Complexity Analysis:
    Time Complexity:
        O(n): A single loop iterates through the gain array.
    Space Complexity:
        O(n): The res list stores all intermediate altitude values.
'''