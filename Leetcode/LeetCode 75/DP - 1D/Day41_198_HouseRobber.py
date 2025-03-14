class Solution:
    def rob(self, nums) -> int:
        if(len(nums)<=2):
            return max(nums)
        res=[]
        res.append(nums[0])
        res.append(nums[1])
        res.append(nums[2]+nums[0])
        for i in range(3,len(nums)):
            res.append(nums[i]+max(res[i-2], res[i-3]))

        return max(res[-1],res[-2])

Solution = Solution()
nums = [1,2,3,1]
print(Solution.rob(nums))
'''
Time Complexity:
The overall time complexity is O(N).
Space Complexity:
The overall space complexity is O(N).


'''