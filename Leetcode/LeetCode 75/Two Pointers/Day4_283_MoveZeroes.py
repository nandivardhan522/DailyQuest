class Solution:
    def moveZeroes(self, nums):
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1

sol=Solution()
nums=[0,1,0,3,12]
sol.moveZeroes(nums)
print(nums)
'''
Time Complexity:
    Iteration: The for loop iterates through the array exactly once, which takes O(n), where 
    n is the size of the array.
    Swapping: Each swap operation takes O(1). In the worst case, there are n swaps, 
    but this is still O(n) overall.
    Overall Time Complexity:
    O(n)
Space Complexity
    The solution operates in place without requiring additional memory, so the space complexity is 
    O(1)
'''
