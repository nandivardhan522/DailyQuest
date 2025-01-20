class Solution:
    def maxOperations(self, nums, k):
        nums.sort()
        i=0
        j=len(nums)-1
        count=0
        while(i<j):
            if(nums[i]+nums[j] == k):
                count+=1
                i+=1
                j-=1
            elif(nums[i] + nums[j] > k):
                j-=1
            else:
                i+=1
        return count
sol=Solution()
nums = [1,2,3,4]
k=5
print(sol.maxOperations(nums,k))
'''
Complexity Analysis:
    Time Complexity:
        Sorting the array takes O(nlogn).
        The two-pointer traversal takes O(n).
        Overall complexity: O(nlogn)
    Space Complexity:
        Sorting is done in-place, and the algorithm uses a constant amount of extra space. 
        Space complexity:O(1)
'''