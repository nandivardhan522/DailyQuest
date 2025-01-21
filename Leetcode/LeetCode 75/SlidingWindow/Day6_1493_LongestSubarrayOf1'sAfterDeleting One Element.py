class Solution:
    def longestSubarray(self, nums):
        zero_indices=[]
        for i in range(len(nums)):
            if(nums[i]==0):
                zero_indices.append(i)
        if(len(zero_indices)<=1):
            return len(nums)-1
        maxi=zero_indices[1]-1
        maxi=max(maxi,len(nums)-1-zero_indices[-2]-1)
        for i in range(1,len(zero_indices)-1):
            length=zero_indices[i+1]-zero_indices[i-1]-2
            maxi=max(length,maxi)
        return maxi
sol=Solution()
nums = [1,1,0,1]
print(sol.longestSubarray(nums))

'''
Complexity Analysis:
    Time Complexity:
        O(n): The loop iterates over the array once to find zero_indices.
        O(k): Where k is the number of zeros, for iterating through zero_indices and calculating lengths.
        Total: O(n), as k is generally smaller than n.
    Space Complexity:
        O(k): Space is used to store indices of zeros in zero_indices.
'''