class Solution:
    def productExceptSelf(self, nums):
        left=[1]*len(nums)
        right=[1]*len(nums)
        res=[]
        for index in range(1,len(nums)):
            left[index]=left[index-1]*nums[index-1]
        for index in range(len(nums)-2,-1,-1):
            right[index]=right[index+1]*nums[index+1]
        for product in range(0,len(nums)):
            res.append(left[product]*right[product])
        return res
sol=Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))

'''
Time Complexity:
    Splitting the String: O(n), where n is the length of the string s.
    Reversing the List: O(w), where w is the number of words.
    Joining the Words: O(n).
    Overall: O(n)
Space Complexity:
    Intermediate List: O(w), where w is the number of words.
    Output String: O(n), as the result string will have a length proportional to n.
    Overall:O(n)
'''