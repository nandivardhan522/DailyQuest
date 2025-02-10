class Solution:
    def successfulPairs(self, spells, potions, success: int):
        potions.sort()
        def getIndex(multiplier):
            if(potions[-1] * multiplier < success):
                return len(potions)
            left = 0
            right = len(potions)
            mid = (left + right) // 2

            while(left <= right):
                if(potions[mid] * multiplier >= success):
                    ind = mid
                    right = mid - 1
                else:
                    left = mid + 1
                mid = ( left + right ) // 2

            return ind

        res=[]
        for i in spells:
            answer = len(potions) - getIndex(i)
            res.append(answer)

        return res

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

Solution = Solution()
print(Solution.successfulPairs(spells,potions,success))

'''
Time Complexity Analysis"
    --> Sorting takes O(m log m), where m is the length of potions.
    --> For each spell in spells (let's say there are n spells), 
        --> we perform a binary search on potions, which takes O(log m).
        
    --> We iterate through n spells, and for each spell, we perform a binary search.
    --> Thus, the final time complexity is O((n+m)logm).

Space Complexity Analysis:
    --> Sorting potions happens in-place, so it requires O(1) extra space.
    --> The result array res stores n values, leading to O(n) space.
    --> Thus, overall space complexity is O(n).
'''