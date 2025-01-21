class Solution:
    def longestOnes(self, nums, k):
        left = 0
        max_length = 0
        zeros_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
sol=Solution()
print(sol.longestOnes(nums,k))

'''
Complexity Analysis:
    Time Complexity:
        Outer Loop: 
            The right pointer iterates through the array: O(n).
        Inner Loop:
            The left pointer iterates through the array only when shrinking the window. 
            Each element is processed at most twice (once by right and once by left): 
            O(n).
        Overall: O(n).
    Space Complexity:
        The algorithm uses a few integer variables and no additional data structures: O(1).
'''
