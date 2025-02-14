import math
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        def getHours(num):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / num)
            return hours

        left, right = 1, max(piles)
        result = right

        while left <= right:
            speed = (left + right) // 2
            hours = getHours(speed)

            if hours <= h:
                result = speed
                right = speed - 1
            else:
                left = speed + 1

        return result
piles = [3,6,7,11]
h = 8

Solution = Solution()

print(Solution.minEatingSpeed(piles,h))

'''
Time Complexity: 
    O(nlogm), where n is the number of piles and 
    m is the maximum value in piles. The binary search takes 
    O(logm) iterations, and each iteration requires O(n) to calculate hours.
Space Complexity: 
    O(1) excluding input storage.
'''