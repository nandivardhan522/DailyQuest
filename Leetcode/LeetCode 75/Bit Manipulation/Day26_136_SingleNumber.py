class Solution:
    def singleNumber(self, nums):
        temp = sum(nums)
        nums=set(nums)
        for i in nums:
            temp -= i*2

        return -temp

nums = [2,2,1]
Solution = Solution()
print(Solution.singleNumber(nums))

'''
Time Complexity:
    sum(nums): O(N)
    set(nums): O(N)
    Loop through set(nums): O(N)
    Overall: O(N)
Space Complexity:
    set(nums) stores unique elements: O(N) in worst case
O   verall: O(N)
'''