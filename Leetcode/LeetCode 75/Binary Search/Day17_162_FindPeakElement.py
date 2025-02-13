class Solution:
    def findPeakElement(self, nums) -> int:
        res=max(nums)
        return nums.index(res)

nums = [1,2,3,1]
Solution = Solution()
print(Solution.findPeakElement(nums))

'''
Time Complexity:
max(nums): O(n), where n is the length of the array because it needs to traverse the entire array to find the maximum.
nums.index(res): O(n) because, in the worst case, the maximum element could be at the end of the array.
Total Time Complexity: O(n)+O(n)=O(n)
Space Complexity:
The space complexity is O(1) as no extra space is used apart from a few variables.'''