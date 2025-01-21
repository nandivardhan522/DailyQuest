class Solution:
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1

sol=Solution()
nums = [1,7,3,6,5,6]
print(sol.pivotIndex(nums))

'''
Complexity Analysis:
    Time Complexity:
        O(n): Calculating total_sum takes O(n).
        A single pass through the array also takes O(n).
        Total complexity: O(n).
    Space Complexity:
        O(1): Uses only scalar variables (total_sum, left_sum).
'''